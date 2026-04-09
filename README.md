Nama    : JUMRA

NIM     : 250907501009

Jurusan : Bisnis Digital

Mata Kuliah : Algoritma dan Pemrograman

# Reorder-Point-Calculator 
Kalkulator untuk menghitung kapan harus restok barang.

## Tampilan kalkulator
![Tampilan Kalkulator](Screenshot%202026-04-08%20194839.png)
![Tampilan About](Screenshot%202026-04-08%20194859.png)

### Untuk Apa Kalkulator Ini Dibuat?
Kalkulator Reorder Point adalah aplikasi web yang membantu pelaku usaha mengetahui kapan waktu yang tepat untuk melakukan restok barang, sehingga tidak kehabisan stok maupun menumpuk modal di gudang.

### Formula/Model Perhitungan
#### Rumus Utama
Reorder Point (ROP) = (Penjualan per Hari × Waktu Tunggu Supplier) + Stok Cadangan

#### Penjelasan Variabel
- Penjualan per Hari = Rata-rata unit barang yang terjual setiap hari
- Waktu Tunggu Supplier = Jumlah hari dari order sampai barang datang
- Stok Cadangan = Buffer stok untuk mengantisipasi ketidakpastian
- Reorder Point = Titik stok minimum saat inilah harus order

#### Contoh Perhitungan
Penjualan per hari  = 50 pcs
Waktu tunggu        = 7 hari
Stok cadangan       = 100 pcs
Stok sekarang       = 200 pcs

ROP        = (50 × 7) + 100 = 450 pcs
Stok habis = 200 ÷ 50       = 4 hari lagi
Status     = 🔴 BAHAYA — stok sudah di bawah ROP, order sekarang!

## Simulasi Penggunaaan
kita gunakan contoh perhitungan di atas misalnya:












