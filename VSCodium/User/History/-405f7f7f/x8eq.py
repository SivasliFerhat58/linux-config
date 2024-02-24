import subprocess

try:
    # Alt süreci çalıştır
    completed_process = subprocess.run(
        ["your_command_here"],
        capture_output=True,  # stdout ve stderr çıktılarını yakala
        text=True,  # Çıktıları metin olarak al
        timeout=10  # Timeout süresi
    )

    # Alt sürecin çıktılarını kontrol et
    print("Standard Output:", completed_process.stdout)
    print("Standard Error:", completed_process.stderr)

except subprocess.TimeoutExpired:
    print("Timeout expired. Alt süreç çalışması durduruldu.")

except Exception as e:
    print("Bir hata oluştu:", e)
