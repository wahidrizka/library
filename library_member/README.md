# library member

### Fitur yang Harus Disediakan:

1. **Status Peminjaman Buku**:
   - Buku di perpustakaan bisa tersedia untuk dipinjam atau tidak. Informasi ini harus ditampilkan dalam formulir buku dan di halaman katalog website.
2. **Data Master Anggota Perpustakaan**:
   - Data utama anggota perpustakaan akan mencakup nomor kartu perpustakaan dan data pribadi seperti nama, alamat, dan email.
3. **Fitur Pesan dan Sosial**:
   - Kita ingin menyediakan fitur pesan dan sosial bagi anggota yang tersedia dalam formulir peminjaman, termasuk widget aktivitas yang direncanakan untuk memungkinkan kolaborasi yang lebih baik.

Ke depan, kita berencana untuk memperkenalkan fitur yang memungkinkan anggota meminjam buku dari perpustakaan.

### Buku

Berikut adalah ringkasan perubahan teknis yang perlu kita lakukan pada buku:

1. **Menambahkan Field "Is Available?"**:
   - Menambahkan field Is Available? untuk menunjukkan ketersediaan buku. Untuk sekarang, field ini akan diatur secara manual, tetapi nantinya bisa diotomatisasi.
2. **Memperluas Logika Validasi ISBN**:
   - Memperluas logika validasi ISBN agar mendukung format ISBN lama yang 10 digit.
3. **Memperluas Halaman Katalog Web**:
   - Memperluas halaman katalog web untuk mengidentifikasi buku yang tidak tersedia dan memungkinkan pengguna untuk memfilter hanya buku yang tersedia.

### Anggota Perpustakaan

Berikut adalah ringkasan perubahan teknis yang perlu dilakukan untuk anggota perpustakaan:

1. Menambahkan Model Baru:
   - Membuat model baru untuk menyimpan informasi seperti nama anggota, nomor kartu perpustakaan, dan informasi kontak seperti email dan alamat.
2. Menambahkan Fitur Diskusi Sosial dan Aktivitas yang Direncanakan:
   - Mengintegrasikan fitur diskusi sosial dan widget aktivitas yang direncanakan untuk mendukung kolaborasi dan interaksi anggota di perpustakaan.
