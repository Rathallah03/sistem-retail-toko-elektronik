# Sistem Retail Toko Elektronik

---
## Anggota Kelompok
- Raihan Athallah  : 101032400117
- Alif Aiman       : 101032400232
- Nabil Muhammad   : 101032400238
---


## Deskripsi
Sistem Retail Toko Elektronik adalah aplikasi sistem informasi berbasis cloud computing sederhana yang digunakan untuk mengelola data produk elektronik, transaksi penjualan, dan dashboard monitoring penjualan.

Sistem ini menggunakan arsitektur 3-tier dengan implementasi 3 Virtual Machine (VM), yaitu:
- VM Frontend
- VM Backend
- VM Database

Project ini dibuat untuk memenuhi Tugas Besar Mata Kuliah Komputasi Awan.

---

## Arsitektur Sistem

### VM Frontend
- IP: 192.168.56.12
- Teknologi:
  - Nginx
  - HTML
  - CSS
  - JavaScript

### VM Backend
- IP: 192.168.56.10
- Teknologi:
  - Python Flask
  - REST API

### VM Database
- IP: 192.168.56.11
- Teknologi:
  - MySQL

---

## Fitur Sistem

### Produk
- Tambah produk
- Edit produk
- Hapus produk
- Manajemen stok
- Harga produk

### Transaksi
- Tambah transaksi penjualan
- Total otomatis
- Riwayat transaksi

### Dashboard
- Total produk
- Total transaksi
- Total penjualan

---

## Struktur Folder

```text
retail-cloud/
│
├── ansible/
├── backend/
├── database/
├── frontend/
├── README.md
└── Vagrantfile
