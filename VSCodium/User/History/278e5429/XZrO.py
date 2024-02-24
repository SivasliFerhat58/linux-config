kelime = input("Kelime: ")

kelime = kelime.upper()
print(kelime)
sayı = input("Sayı: ")

harfler = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]

for i in kelime:
        index = harfler.index(i)
        index += int(sayı)
        if index >= len(harfler):
            index -= len(harfler)

            """
        if i == len(kelime)-1:
            print(harfler[index])
        else:   """
        print(harfler[index],end="")