from bluetooth import *

# Bluetooth cihazlarını tarar ve bulunan cihazları listeler
def discover_devices():
    nearby_devices = discover_devices(duration=8, lookup_names=True)
    print("Bulunan cihazlar:")
    for addr, name in nearby_devices:
        print(f"{addr} - {name}")

# Bluetooth etkileşimlerini dinler
def listen_for_interactions():
    server_sock = BluetoothSocket(RFCOMM)
    server_sock.bind(("", PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    uuid = "00001101-0000-1000-8000-00805F9B34FB"  # SPP (Serial Port Profile) için standart UUID
    advertise_service(server_sock, "SampleServer",
                      service_id=uuid,
                      service_classes=[uuid, SERIAL_PORT_CLASS],
                      profiles=[SERIAL_PORT_PROFILE])

    print(f"Dinlenen port: {port}")

    client_sock, client_info = server_sock.accept()
    print(f"Bağlanan cihaz: {client_info}")

    try:
        while True:
            data = client_sock.recv(1024)
            if len(data) == 0:
                break
            print(f"Alınan veri: {data}")
    except IOError:
        pass

    print("Bağlantı kapatılıyor...")
    client_sock.close()
    server_sock.close()
    print("Bağlantı kapatıldı.")

if __name__ == "__main__":
    print("Bluetooth cihazları tarama başlatılıyor...")
    discover_devices()
    print("Bluetooth etkileşimlerini dinleme başlatılıyor...")
    listen_for_interactions()
