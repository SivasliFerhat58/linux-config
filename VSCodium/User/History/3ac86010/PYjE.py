import discord
from discord.ext import commands
import subprocess
import time
import json

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)
adminid = 760426163369017375
guildid = 1187719494156685383

def kelime_arama(dosya_adı, aranan_kelime):
    with open(dosya_adı, 'r') as dosya:
        icerik = dosya.read()
        if aranan_kelime in icerik:
            return True
        else:
            print(aranan_kelime)


def load_json(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data


def save_json(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Progress: 90%"))

@client.command()
async def teslim(ctx):
    missions_file = 'chapter.json'
    points_file = 'points.json'

    chapterdata = load_json(missions_file)
    pointdata = load_json(points_file)

    mod = chapterdata["facetoface"]

    if ctx.message.attachments:
        attachment = ctx.message.attachments[0]
        filename = f"{ctx.author.id}.js"
        await attachment.save(f"files/{filename}")
        file = f"files/{filename}"
        time.sleep(2)

        result = subprocess.run(["node", file], capture_output=True, text=True,timeout=2)
        print(result)
        output = cleaned_output = result.stdout.replace(
            '\n', '').replace('\r', '')
        print(cleaned_output)
        user_chapter = str(ctx.author.id)
        user_data = pointdata.get(user_chapter, {"chapter": 0})

        data_id = chapterdata["chapters"][user_data["chapter"]-1]["lessons"][user_data["lesson"]-1]
        print(data_id["keywords"])
        if result.stderr:
            await ctx.send(f"Kodunuz hata veriyor. \n Error:```{result.stderr}```")

        elif data_id["output"] == output:
            eksik_kod = False
            for keyword in data_id["keywords"]:
                if not kelime_arama(file, keyword):
                    await ctx.send("Kodunuz doğru sonucu dönderse de istenilen şekilde yazılmamıştır.")
                    eksik_kod = True
                    return eksik_kod
            if eksik_kod:
                puan = 0

            else:
                await ctx.send("Tebrikler, görevi tamamladınız.")
                #!UNUTMA
#Todo                guild = client.get_guild(guildid)
#Todo                channels = guild.channels
#Todo                next_channel = discord.utils.get(channels, name=f"chapter_{user_data['chapter']}")

                if mod == 1:
                    puan = 0
                    data_id["solved"] += 1
                    
                elif data_id["solved"] == 0:
                    puan = data_id["base_point"] + data_id["first_point"]
                    data_id["solved"] += 1

                elif data_id["solved"] == 1:
                    puan = data_id["base_point"] + data_id["second_point"]
                    data_id["solved"] += 1

                elif data_id["solved"] == 2:
                    puan = data_id["base_point"] + data_id["third_point"]
                    data_id["solved"] += 1

                else:
                    puan = data_id["base_point"]
                    data_id["solved"] += 1
 
            new_lesson = user_data["lesson"] + 1

            if new_lesson > len(chapterdata["chapters"][user_data["chapter"]-1]["lessons"]):
                new_chapter = user_data["chapter"] + 1
                if new_chapter > len(chapterdata["chapters"])+1:
                    await ctx.send("Tebrikler, tüm görevleri tamamladınız.")
                user_data["chapter"] = new_chapter
                user_data["lesson"] =  1
            else:
                new_lesson = user_data["lesson"] + 1
                user_data["lesson"] = new_lesson
                new_chapter = user_data["chapter"]

            user_data[f"chapter-{new_chapter}_lesson-{new_lesson-1}"] = puan
            pointdata[user_chapter] = user_data
            save_json(points_file, pointdata)
            save_json(missions_file, chapterdata)


        else:
            await ctx.send(f"Kodunuz yanlış sonucu dönderiyor. \n Output:```{output}```")

    else:
        await ctx.send("Dosya bulunamadı.")


@client.command()
async def sıralama(ctx):
    if ctx.author.id != adminid:
        await ctx.send("Bu komutu kullanmak için yetkiniz yok.")
        return
    points_file = 'points.json'
    pointdata = load_json(points_file)

    puanlar = {}

    # Her kullanıcı için puanları topla
    for kullanici_id, bilgiler in pointdata.items():
        toplam_puan = 0
        for chapter, puan in bilgiler.items():
            if chapter.startswith('chapter_'):
                toplam_puan += puan
        puanlar[kullanici_id] = toplam_puan

    # Puanlara göre sırala
    sirali_puanlar = sorted(puanlar.items(), key=lambda x: x[1], reverse=True)

    # Sonucu yazdır
    mesaj = ""
    for sira, (kullanici_id, toplam_puan) in enumerate(sirali_puanlar, start=1):
        # Kullanıcı ID'sini etiketle ve mesajı oluştur
        kullanici_etiketi = f"<@{kullanici_id}>"
        mesaj += f"{sira}. Kullanıcı: {kullanici_etiketi}, Toplam Puan: {toplam_puan}\n"
    mesaj += ""
    await ctx.send(mesaj)

@client.command()
async def mod(ctx):
    missions_file = 'chapter.json'
    chapterdata = load_json(missions_file)
    index = chapterdata["facetoface"]
    if index == 1:
        await ctx.send("Online modu açıldı")
        chapterdata["facetoface"] = 0

    else:
        await ctx.send("Yüz yüze modu açıldı.")
        chapterdata["facetoface"] = 1

    save_json(missions_file, chapterdata)

@client.command()
async def modkontrol(ctx):
    missions_file = 'chapter.json'
    chapterdata = load_json(missions_file)
    index = chapterdata["facetoface"]
    if index == 1:
        await ctx.send("Yüz yüze modu açık")

    else:
        await ctx.send("Online modu açık")

@client.command()
async def yardım(ctx):
    await ctx.send("""
    Botu kullanmak için **!teslim** komutunu kullanıp javascript dosyanızı yüklemeniz gerekiyor. Botun aynı anda bir kaç dosyayı çalıştırıyor olabileceğini göz önünde bulundurarak biraz sabırlı olun. Biraz beklemenin ardından bot size kodunuzun dönütünü verecektir.
    """)

@client.command()
async def test(ctx):
    if ctx.message.attachments:
        attachment = ctx.message.attachments[0]
        filename = f"{ctx.author.id}.js"
        await attachment.save(f"files/{filename}")
        file = f"files/{filename}"
        result = subprocess.run(["node", file], capture_output=True, text=True)

        output = cleaned_output = result.stdout
        print(cleaned_output)
        if result.stderr:
            await ctx.send(f"{ctx.author.mention} - Kodunuz hata veriyor. \n Error:```{result.stderr}```")
        else:
            await ctx.send(f"{ctx.author.mention} - Output:```{output}```")

@client.command()
async def puanekle(ctx,user: discord.User, point: int):
    if ctx.author.id != adminid:
        await ctx.send("Bu komutu kullanmak için yetkiniz yok.")
        return
    points_file = 'points.json'
    pointdata = load_json(points_file)

    user_chapter = str(user.id)
    user_data = pointdata.get(user_chapter, {"extra_point": 0})

    user_data["extra_point"] += point
    pointdata[user_chapter] = user_data
    save_json(points_file, pointdata)
    await ctx.send(f"{user.mention} - {point} puan eklendi.")

client.run("MTE5NzQxMTk1NjI0MDQxNjgxMA.Gwu2HV.mqTzS2Lwp5YTl6mQ1EVvYsksu1L7eCtzNP64ac")
