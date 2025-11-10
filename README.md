# Portofolio Software Quality Assurance (SQA) - Umar Abdul Aziz

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Umar%20Abdul%20Aziz-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/umar-abdul-aziz-b95435273)
[![GitHub](https://img.shields.io/badge/GitHub-Portofolio-181717?style=flat&logo=github)](https://github.com/[NAMA_PENGGUNA_ANDA]/[NAMA_REPOSITORI_INI])

## 🌟 Tentang Saya

Selamat datang di portofolio SQA saya!

Saya Umar Abdul Aziz, seorang mahasiswa S1 Sistem Informasi di UIN Sunan Ampel Surabaya yang memiliki fokus kuat pada **Software Quality Assurance (SQA)** dan **Cyber Security**.

Repositori ini adalah kumpulan proyek yang saya buat untuk menunjukkan pemahaman dan kemampuan saya dalam pengujian perangkat lunak, mulai dari metodologi manual hingga otomatisasi teknis.

---

## 📂 Daftar Proyek Portofolio

Repositori ini dibagi menjadi tiga bagian utama:

### 1. Pengujian Manual (Manual Testing)

Menunjukkan kemampuan saya dalam merencanakan, mendokumentasikan, dan mengeksekusi tes secara metodis untuk menemukan *bug*.

* **Aplikasi yang Diuji:** `https://www.saucedemo.com/`
* **Dokumen:**
    * **[Dokumen Skenario Tes (Test Case)](/1_Manual_Testing/Test_Case_SauceDemo.pdf)**: Berisi 14 skenario tes (Positif & Negatif) yang mencakup alur Login, Inventaris, dan Keranjang Belanja.
    * **[Laporan Bug (Bug Report)](/1_Manual_Testing/Laporan_Bug_SauceDemo.pdf)**: Berisi 4 temuan *bug* fungsional dan visual (Severity High & Medium) yang ditemukan saat menguji menggunakan akun `problem_user`.

### 2. Otomatisasi Tes (Selenium dengan Python)

Menunjukkan kemampuan saya untuk menulis skrip tes otomatis *end-to-end* menggunakan salah satu *tool* standar industri terpopuler, Selenium.

* **Folder Proyek:** `2_Automation_Selenium_Python/`
* **Tools:** Python, Selenium, Webdriver-Manager
* **Skenario yang Diotomatisasi:**
    * `test_login_sukses.py`: Memvalidasi login berhasil menggunakan *credentials* yang valid.
    * `test_login_gagal.py`: Memvalidasi pesan *error* yang benar muncul saat menggunakan *password* yang salah.
* **Cara Menjalankan:**
    ```bash
    # 1. Pastikan Python terinstal
    # 2. Instal library yang dibutuhkan
    pip install selenium webdriver-manager
    
    # 3. Jalankan tes
    python test_login_sukses.py
    python test_login_gagal.py
    ```

### 3. Otomatisasi Tes (Cypress dengan JavaScript)

Menunjukkan kemampuan saya untuk beradaptasi dengan *framework* modern dan membandingkan pendekatan *testing*.

* **Folder Proyek:** `3_Automation_Cypress_JS/`
* **Tools:** JavaScript, Cypress, Node.js
* **Skenario yang Diotomatisasi:**
    * `login.cy.js`: Berisi 2 *test case* (`it` blocks) untuk memvalidasi alur login sukses (TC-L-001) dan alur login gagal (TC-L-002).
* **Cara Menjalankan:**
    ```bash
    # 1. Pastikan Node.js terinstal
    # 2. Instal dependensi (dari dalam folder proyek)
    npm install
    
    # 3. Buka Cypress Test Runner
    npx cypress open
    
    # 4. Klik 'login.cy.js' untuk menjalankan tes
    ```

### 4. Otomatisasi Tes API (Postman)

Menunjukkan kemampuan saya dalam menguji logika *backend* (server) melalui API, lengkap dengan skrip tes otomatis di dalam Postman.

* **Folder Proyek:** `4_Automation_API_Postman/`
* **Tools:** Postman
* **Target API:** `https://reqres.in/`
* **Skenario yang Diotomatisasi:**
    * **GET** (List Users): Memvalidasi status `200` dan integritas data (jumlah pengguna).
    * **POST** (Create User): Memvalidasi status `201` dan kesesuaian data yang dikirim dengan yang diterima.
    * **PUT** (Update User): Memvalidasi status `200` dan data berhasil diperbarui.
    * **DELETE** (Delete User): Memvalidasi status `204` (No Content).
* **Cara Menggunakan:**
    1.  Unduh file **[Portofolio_Postman.json](/4_Automation_API_Postman/Portofolio_Tes_API_-_reqres.in.postman_collection.json)** dari folder proyek.
    2.  Buka Postman, klik **"Import"**.
    3.  Pilih file `.json` tersebut. *Collection* akan muncul di panel kiri Anda.
    4.  Jalankan setiap *request* dan periksa tab **"Test Results"** untuk melihat hasil validasi otomatis.

### 5. Pengujian Keamanan Dasar (OWASP ZAP)

Menunjukkan pemahaman dasar tentang *cyber security* dalam konteks SQA dengan melakukan *Dynamic Application Security Testing* (DAST) dasar.

* **Folder Proyek:** `5_Security_Testing_ZAP/`
* **Tools:** OWASP ZAP (Zed Attack Proxy)
* **Target Aplikasi:** OWASP Juice Shop (Aplikasi yang sengaja dibuat rentan untuk latihan).
* **Dokumen:**
    * **[Laporan Vulnerability Security.pdf](/5_Security_Testing_ZAP/Laporan_Vulnerability_Security.pdf)**: Berisi laporan dari 3 temuan kerentanan (Vulnerability) teratas (kategori High/Medium) yang ditemukan oleh pemindai otomatis ZAP, lengkap dengan deskripsi dan rekomendasi perbaikan.

---

## 💡 Kontak

Terima kasih telah meninjau portofolio saya. Saya sangat terbuka untuk diskusi, *feedback*, dan kesempatan magang.

* **LinkedIn:** [https://www.linkedin.com/in/umar-abdul-aziz-b95435273](https://www.linkedin.com/in/umar-abdul-aziz-b95435273)
* **Email:** [emailanda@domain.com]