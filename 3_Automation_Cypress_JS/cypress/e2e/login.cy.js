// 'describe' adalah cara mengelompokkan tes. Ini adalah "Test Suite" kita.
describe('Test Suite: Fungsionalitas Login saucedemo.com', () => {

  // 'beforeEach' adalah hook yang berjalan SEBELUM setiap tes ('it' block).
  // Ini bagus untuk mengulang langkah yang sama, seperti mengunjungi website.
  beforeEach(() => {
    // 1. Kunjungi halaman login
    cy.visit('https://www.saucedemo.com/');
  });

  // -----------------------------------------------------------------

  // 'it' adalah test case individu kita.
  it('TC-L-001: Harus berhasil login dengan standard_user', () => {
    
    // --- Langkah Tes (Test Steps) ---
    
    // 2. Masukkan username (Cypress menggunakan CSS Selector)
    // cy.get() untuk mencari elemen
    // .type() untuk mengetik
    cy.get('#user-name').type('standard_user');
    
    // 3. Masukkan password
    cy.get('#password').type('secret_sauce');
    
    // 4. Klik tombol login
    cy.get('#login-button').click();

    // --- Validasi (Assert) ---
    // Di Cypress, validasi (assert) sudah built-in.
    // .should('eq', ...) berarti "harus sama dengan"
    cy.url().should('eq', 'https://www.saucedemo.com/inventory.html');
    
    // Kita juga bisa cek apakah halaman inventaris benar-benar muncul
    cy.get('.inventory_list').should('be.visible');
  });

  // -----------------------------------------------------------------

  it('TC-L-002: Harus menampilkan pesan error dengan password salah', () => {
    
    // --- Langkah Tes (Test Steps) ---
    
    // 2. Masukkan username
    cy.get('#user-name').type('standard_user');
    
    // 3. Masukkan password SALAH
    cy.get('#password').type('password_salah_123');
    
    // 4. Klik tombol login
    cy.get('#login-button').click();

    // --- Validasi (Assert) ---
    
    // Kita cari elemen pesan error
    // .should('be.visible') untuk memastikan elemennya terlihat
    // .should('have.text', ...) untuk memeriksa teks di dalamnya
    cy.get('h3[data-test="error"]')
      .should('be.visible')
      .should('have.text', 'Epic sadface: Username and password do not match any user in this service');
  });

});