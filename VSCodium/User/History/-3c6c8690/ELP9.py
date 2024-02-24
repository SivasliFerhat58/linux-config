import re

# Dosya adını ve yolunu belirtin
dosya_yolu = "./data/data1.txt"
yeni_dosya_yolu = "temizlenmis_metin.txt"

try:
    # Metin dosyasını oku
    with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
        metin = dosya.readlines()

    # Temizlenmiş metni tutacak bir liste oluştur
    temizlenmis_metin = []

    # Her satırı işle
    for satir in metin:
        # Noktalama işaretleri, rakamlar ve boşlukları kaldır
        temiz_satir = re.sub(r'[^\w\s]', '', satir)
        temiz_satir = re.sub(r'\d+', '', temiz_satir)
        temiz_satir = temiz_satir.strip()  # Satırın başındaki ve sonundaki boşlukları kaldır
        if temiz_satir:  # Boş olmayan satırları ekle
            temizlenmis_metin.append(temiz_satir)

    # Temizlenmiş metni yeni bir dosyaya yaz
    with open(yeni_dosya_yolu, 'w', encoding='utf-8') as yeni_dosya:
        for satir in temizlenmis_metin:
            yeni_dosya.write(satir + '\n')

    print("Metin başarıyla temizlendi ve yeni dosyaya yazıldı.")

except FileNotFoundError:
    print("Belirtilen dosya bulunamadı.")
except Exception as e:
    print("Bir hata oluştu:", str(e))
