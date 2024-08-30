# library
 Odoo app to manage a book library. A learning project to better explore Odoo development

## Fitur Pertama: Katalog Buku

Fitur pertama yang akan kita implementasikan adalah katalog buku. Katalog ini memungkinkan kita menyimpan catatan buku-buku yang ada di perpustakaan, lengkap dengan detail yang relevan. Selain itu, kita juga ingin membuat katalog ini tersedia melalui website publik, sehingga buku-buku yang tersedia bisa dilihat oleh umum.

#### Data yang Harus Dimiliki Buku Perpustakaan:
- Judul
- Penulis
- Penerbit
- Tanggal Terbit
- Gambar Sampul
- ISBN (International Standard Book Number) dengan validasi digit cek
- Status Aktif, yang menunjukkan buku-buku yang seharusnya tersedia secara publik di website

#### Pengaturan Grup Pengguna:
Seperti aplikasi dasar Odoo lainnya, aplikasi Perpustakaan ini akan memiliki dua grup pengguna:
1. **Library User** (Pengguna Perpustakaan)
2. **Library Manager** (Manajer Perpustakaan)

Pengguna pada level **User** diharapkan bisa melakukan semua operasi harian, sementara pengguna **Manager** juga dapat mengedit konfigurasi aplikasi.

Untuk fitur katalog buku, pengeditan catatan buku akan dibatasi hanya untuk Manajer. Rincian aturan akses sebagai berikut:
- **Manajer Perpustakaan** dapat mengedit buku.
- **Pengguna Perpustakaan** dan **Pengguna Publik** yang menggunakan website hanya dapat melihat buku.