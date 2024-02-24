import subprocess

try:
    # Alt süreci başlat
    process = subprocess.Popen(
        ["python3", "a.py"],  # Senaryo.py adlı dosyayı çalıştırır. Bunu kendi senaryo dosyanızla değiştirin.
        stdout=subprocess.PIPE,  # Standart çıktıyı yakala
        stderr=subprocess.PIPE,  # Standart hata çıktısını yakala
        universal_newlines=True,  # Çıktıları str olarak al
    )

    # Alt sürecin çıktılarını ve hatalarını al
    stdout, stderr = process.communicate(timeout=2)

    # Çıktıları yazdır
    print("Çıktı:", stdout)
    print("Hata:", stderr)

except subprocess.TimeoutExpired:
    # Timeout durumunda çıktıyı al ve kullan
    stdout, stderr = process.communicate()
    print("Timeout. Ana kadarki çıktılar:")
    print("Çıktı:", stdout)
    print("Hata:", stderr)

except Exception as e:
    print("Bir hata oluştu:", e)
