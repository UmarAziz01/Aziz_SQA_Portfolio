# --- Import Library yang Dibutuhkan ---
from selenium import webdriver
from selenium.webdriver.common.by import By # Untuk mencari elemen (misal: berdasarkan ID, Nama, CSS)
from selenium.webdriver.chrome.service import Service # Untuk menjalankan driver browser
from webdriver_manager.chrome import ChromeDriverManager # Untuk mengelola driver Chrome secara otomatis
import time # Untuk memberi jeda waktu

# --- Setup WebDriver ---
# Ini akan mengunduh dan menginstal driver Chrome yang sesuai secara otomatis
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Membuka browser dan mengarahkan ke URL
driver.get("https://www.saucedemo.com/")
driver.maximize_window() # Memaksimalkan jendela browser
print("Halaman login berhasil dibuka.")

try:
    # --- Langkah-Langkah Tes (Test Steps) ---

    # 1. Masukkan username (TC-L-001)
    # Kita mencari elemen berdasarkan ID-nya: "user-name"
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    
    # 2. Masukkan password (TC-L-001)
    # Kita mencari elemen berdasarkan ID-nya: "password"
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    
    # 3. Klik tombol 'Login' (TC-L-001)
    # Kita mencari elemen berdasarkan ID-nya: "login-button"
    driver.find_element(By.ID, "login-button").click()
    
    print("Mencoba login dengan 'standard_user'...")
    
    # --- Validasi (Assert) ---
    # Ini adalah bagian terpentING dari tes: memeriksa apakah hasilnya sesuai harapan.
    
    # Kita beri jeda 1 detik agar halaman selesai loading
    time.sleep(1)
    
    # Ambil URL browser saat ini
    actual_url = driver.current_url
    
    # URL yang kita harapkan setelah login sukses
    expected_url = "https://www.saucedemo.com/inventory.html"
    
    print(f"URL Sebenarnya: {actual_url}")
    print(f"URL Diharapkan: {expected_url}")
    
    # Melakukan Pengecekan
    if actual_url == expected_url:
        print("--- HASIL: TEST CASE LULUS (PASSED) ---")
        print("Login berhasil dan pengguna diarahkan ke halaman inventaris.")
    else:
        print("--- HASIL: TEST CASE GAGAL (FAILED) ---")
        print(f"URL tidak sesuai. Pengguna tidak diarahkan ke halaman inventaris.")

except Exception as e:
    # Jika terjadi error (misal: elemen tidak ditemukan), tes dianggap gagal
    print(f"--- HASIL: TEST CASE GAGAL (FAILED) ---")
    print(f"Terjadi error saat eksekusi: {e}")

finally:
    # --- Cleanup ---
    # Beri jeda 3 detik agar Anda bisa melihat hasilnya di browser
    time.sleep(3)
    
    # Tutup browser
    driver.quit()
    print("Browser telah ditutup.")