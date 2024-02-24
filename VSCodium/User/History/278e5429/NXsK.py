kelime = input("Kelime: ")

kelime = kelime.capitalize()
print(kelime)
sayı = input("Sayı: ")

harfler = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]

for i in kelime:
        index = harfler.index(i)
        print(index)
        index += int(sayı)
        if index >= len(harfler):
            index -= len(harfler)
        print(harfler[index],end="")