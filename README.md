<p align="center">
  <img src="https://img.shields.io/badge/Architecture-3--Tier%20VM-blue?style=for-the-badge" alt="Architecture">
  <img src="https://img.shields.io/badge/Focus-Cloud%20Computing-orange?style=for-the-badge" alt="Focus">
</p>

<h1 align="center">Sistem Retail Toko Elektronik</h1>
<p align="center">Aplikasi Sistem Informasi Retail Berbasis Cloud Computing Sederhana</p>

---

## 👥 Anggota Kelompok

| Nama | NIM |
| :--- | :--- |
| **Raihan Athallah** | 101032400117 |
| **Alif Motor** | - |
| **Nabil Muhammad Ar Rasya** | 101032400238 |

---

## Deskripsi

**Sistem Retail Toko Elektronik** adalah aplikasi sistem informasi berbasis cloud computing sederhana yang digunakan untuk mengelola data produk elektronik, transaksi penjualan, dan dashboard monitoring penjualan.

Sistem ini diimplementasikan menggunakan arsitektur **3 tier Virtual Machine**:
- VM Frontend
- VM Backend
- VM Database

---

## Arsitektur Sistem

Proyek ini dibangun di atas infrastruktur lokal menggunakan **Vagrant** dan diorkestrasi dengan **Ans  ible** menggunakan 3 VM utama:

### VM Frontend
* **IP Address:** `192.168.56.12`
* **Teknologi:** * ![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat-square&logo=nginx&logoColor=white) sebagai Web Server
  * HTML5, CSS3, & Vanilla JavaScript

### VM Backend
* **IP Address:** `192.168.56.10`
* **Teknologi:** * ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) Flask Framework
  * RESTful API Development

### VM Database
* **IP Address:** `192.168.56.11`
* **Teknologi:** * ![MySQL](https://img.shields.io/badge/MySQL-00758F?style=flat-square&logo=mysql&logoColor=white) Relational Database

---

## Fitur Utama Sistem

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

## Struktur Folder Proyek

```text
retail-cloud/
│
├── ansible/
├── backend/
├── database/
├── frontend/
├── README.md
└── Vagrantfile
