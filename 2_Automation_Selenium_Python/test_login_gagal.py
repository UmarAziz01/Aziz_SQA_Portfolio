# --- Import Library yang Dibutuhkan ---
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- Setup WebDriver ---
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
print("Halaman login berhasil dibuka.")

try:
    # --- Langkah-Langkah Tes (Test Steps) ---

    # 1. Masukkan username (TC-L-002)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    
    # 2. Masukkan password SALAH (TC-L-002)
    driver.find_element(By.ID, "password").send_keys("password_salah_123")
    
    # 3. Klik tombol 'Login' (TC-L-002)
    driver.find_element(By.ID, "login-button").click()
    
    print("Mencoba login dengan password salah...")
    
    # --- Validasi (Assert) ---
    # Kita ingin memvalidasi bahwa pesan error yang benar MUNCUL.
    
    time.sleep(1) # Beri jeda agar pesan error sempat muncul
    
    # Kita cari elemen pesan error. Cara terbaik adalah menggunakan CSS SELECTOR
    # Kita mencari tag <h3> yang memiliki atribut data-test="error"
    error_element = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    
    # Ambil teks dari elemen error tersebut
    actual_error_message = error_element.text
    
    # Teks error yang kita harapkan
    expected_error_message = "Epic sadface: Username and password do not match any user in this service"
    
    print(f"Pesan Error Sebenarnya: {actual_error_message}")
    print(f"Pesan Error Diharapkan: {expected_error_message}")
    
    # Melakukan Pengecekan
    if actual_error_message == expected_error_message:
        print("--- HASIL: TEST CASE LULUS (PASSED) ---")
        print("Login gagal DAN pesan error yang ditampilkan sudah sesuai.")
    else:
        print("--- HASIL: TEST CASE GAGAL (FAILED) ---")
        print("Pesan error yang ditampilkan TIDAK SESUAI harapan.")

except Exception as e:
    # Jika elemen error tidak ditemukan (misal: malah berhasil login), tes dianggap gagal
    print(f"--- HASIL: TEST CASE GAGAL (FAILED) ---")
    print(f"Tidak dapat menemukan elemen pesan error, atau terjadi error lain: {e}")

finally:
    # --- Cleanup ---
    time.sleep(3)
    driver.quit()
    print("Browser telah ditutup.")