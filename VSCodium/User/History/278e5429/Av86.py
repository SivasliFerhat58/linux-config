kelime = input("Kelime: ")
sayı = input("Sayı: ")

harfler = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]

for i in kelime:
    if i in harfler:
        index = harfler.index(i)
        index += int(sayı)
        if index >= len(harfler):
            index -= len(harfler)
        print(harfler[index],end="")
    else:
        print(i,end="")