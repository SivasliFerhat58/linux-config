kelime = input("Şifrelemek İstediğin Kelimeyi Gir: ").upper()
sayı = int(input("Kaç Harf Kaydırmak İstiyorsun: "))

harfler = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]

for harf in kelime:
    index = harfler.index(harf)
    index += sayı
    if index > len(harfler):
        index = index - len(harfler)
    print(harfler[index],end="")
    #deneme 3
