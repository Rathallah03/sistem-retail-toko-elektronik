CREATE DATABASE retail_db;

USE retail_db;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama_produk VARCHAR(255),
    kategori VARCHAR(100),
    harga DECIMAL(10,2),
    stok INT
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tanggal DATETIME,
    total DECIMAL(10,2)
);

CREATE TABLE transaction_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id INT,
    product_id INT,
    qty INT,
    subtotal DECIMAL(10,2),

    FOREIGN KEY (transaction_id)
    REFERENCES transactions(id),

    FOREIGN KEY (product_id)
    REFERENCES products(id)
);