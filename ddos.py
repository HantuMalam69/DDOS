import threading
import requests
import time
# Tools by Marketing Ngaco!
# Konfigurasi
TARGET_URL = 'https://mengundang.gerim.is/amp/RUBY8000/RUBY8000.html'  # Ganti dengan URL target Anda
NUMBER_OF_THREADS = 100                   # Jumlah thread yang akan dijalankan secara bersamaan
REQUESTS_PER_THREAD = 10                  # Jumlah permintaan per thread

def send_requests():
    for _ in range(REQUESTS_PER_THREAD):
        try:
            response = requests.get(TARGET_URL)
            print(f'Status Kode: {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f'Permintaan gagal: {e}')

def main():
    threads = []
    start_time = time.time()
    
    # Membuat dan memulai thread
    for _ in range(NUMBER_OF_THREADS):
        thread = threading.Thread(target=send_requests)
        thread.start()
        threads.append(thread)
    
    # Menunggu semua thread selesai
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    print(f'Total waktu yang dibutuhkan: {end_time - start_time} detik')

if __name__ == "__main__":
    main()
