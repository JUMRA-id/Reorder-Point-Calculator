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

#### Fitur
- Hitung Reorder Point secara otomatis
- Status stok: Aman, Waspada, atau Bahaya
- Visualisasi bar kondisi stok
- Estimasi berapa hari stok akan habis
- Estimasi kapan harus order ulang

#### Contoh Perhitungan
- Penjualan per hari  = 50 pcs
- Waktu tunggu        = 7 hari
- Stok cadangan       = 100 pcs
- Stok sekarang       = 200 pcs
###### maka hasilnya:
- ROP        = (50 × 7) + 100 = 450 pcs
- Stok habis = 200 ÷ 50       = 4 hari lagi
- Status     = 🔴 BAHAYA — stok sudah di bawah ROP, order sekarang!

## Simulasi Penggunaaan
kita gunakan contoh perhitungan di atas misalnya:
![Tampilan Kalkulator](Screenshot%202026-04-09%20191846.png)
###### keterangan:
- 450 pcs di layar atas = artinya ketika stok tinggal 450 pcs, saat itulah harus order
- Reorder point: 450 pcs = hasil dari rumus (50×7)+100
- Stok habis dalam: 4 hari = dengan stok 200 dan jual 50/hari, stok habis dalam 4 hari
- Order lagi: Sekarang! = karena stok sekarang (200) sudah di bawah ROP (450), artinya sudah terlambat, harus order sekarang juga
- Bar merah = posisi stok ada di zona bahaya
- Badge merah = konfirmasi status kritis

### Status Stok
- Jika  Stok ≤ ROP         = 🔴 BAHAYA   = Order sekarang!
- Jika  Stok ≤ ROP × 1.5   = 🟡 WASPADA  = Segera siapkan order
- Jika  Stok > ROP × 1.5   = 🟢 AMAN     = Stok masih cukup

## Penjelasan APP.PY 
Menggunakan Flask untuk membuat kalkulatornya karena Flask adalah framework Python yang ringan dan cocok untuk membuat web app sederhana. Dengan Flask, logika perhitungan Python bisa langsung diakses lewat browser

##### Baris 1
<img width="803" height="34" alt="image" src="https://github.com/user-attachments/assets/add2c5ef-a941-4269-8b85-39a55fd6dfe4" />

##### Mengimpor komponen/alat-alat Flask yang dibutuhkan:
- Flask = membuat aplikasi web/framework-nya
- render_template = menampilkan file HTML ke browser/untuk tampilkan HTML
- request = membaca data yang dikirim dari browser/untuk terima data dari form
- jsonify = mengubah hasil Python menjadi format JSON/untuk kirim hasil balik ke web

##### Baris 3
<img width="399" height="41" alt="image" src="https://github.com/user-attachments/assets/2f20d969-58b6-498c-b36b-d936041e4dbd" />

Membuat aplikasi Flasknya . __name__ memberitahu Flask lokasi folder proyek agar bisa menemukan file template dan static.

##### Baris 5-7
<img width="609" height="100" alt="image" src="https://github.com/user-attachments/assets/e8e2a463-82d4-40ea-b30e-525a1667caa6" />
Mendaftarkan halaman utama (/). Ketika pengguna membuka localhost:5000, fungsi index() dipanggil dan menampilkan index.html.

Tipe data: string (nama file HTML)

##### Baris 9-11
<img width="573" height="94" alt="image" src="https://github.com/user-attachments/assets/0a7b99b2-1db5-43a5-980d-04ce64536f9f" />

Mendaftarkan hitung yang hanya menerima metode POST. Dipanggil saat tombol HITUNG diklik. Data dikirim secara tersembunyi, bukan lewat URL.

data = request.get_json() = 
Membaca data JSON yang dikirim dari JavaScript di browser. Hasilnya berupa dictionary Python.

##### Baris 13-16
<img width="927" height="126" alt="image" src="https://github.com/user-attachments/assets/33745211-7119-4eb9-8ac2-8712f5c7b9f9" />

Mengambil masing-masing nilai dari data JSON dan mengkonversinya ke tipe float. Jika nilai tidak dikirim, default-nya adalah 0.

Tipe data: float

##### Baris 19-22
<img width="1063" height="177" alt="image" src="https://github.com/user-attachments/assets/a5bdd1a7-c8aa-4fd0-ae5a-4d3055945951" />
Validasi input. Jika penjualan per hari atau waktu tunggu bernilai 0 atau negatif, server langsung mengembalikan pesan error dengan kode HTTP 400 tanpa melakukan kalkulasi.

<img width="756" height="907" alt="image" src="https://github.com/user-attachments/assets/70e1156e-b5bc-4060-8514-09f948afa457" />

##### Baris 26-35
<img width="1108" height="377" alt="image" src="https://github.com/user-attachments/assets/20162e57-4509-44be-9b6d-4728f58b1e77" />

- Rumus utama Reorder Point. Hasil perkalian penjualan dan waktu tunggu ditambah stok cadangan.
- Menghitung berapa hari sampai stok habis. Kondisi if stok_sekarang > 0 mencegah pembagian dengan nol.
- Menghitung berapa hari lagi sebelum harus order. max(0, hari_order) memastikan nilainya tidak pernah negatif — jika minus berarti sudah harus order sekarang.

Tipe data: float

##### Baris 37-43
<img width="990" height="290" alt="image" src="https://github.com/user-attachments/assets/0d2c946a-7570-480d-8205-60378331da71" />

Logika penentuan status stok berdasarkan perbandingan stok sekarang dengan ROP.
- Jika  Stok ≤ ROP         = 🔴 BAHAYA   = Order sekarang!
- Jika  Stok ≤ ROP × 1.5   = 🟡 WASPADA  = Segera siapkan order
- Jika  Stok > ROP × 1.5   = 🟢 AMAN     = Stok masih cukup

Tipe data: string

##### Baris 48-49
<img width="743" height="99" alt="image" src="https://github.com/user-attachments/assets/01188fb7-ea72-42f5-98db-cf1666546669" />
Fungsi pembantu untuk memformat angka ke gaya penulisan Indonesia. Contoh: 25000 menjadi 25.000 pcs.

Tipe data: string

##### Baris 51-58
<img width="1210" height="253" alt="image" src="https://github.com/user-attachments/assets/3859f0f7-ceab-4334-a9a5-ae4fea682066" />
Mengirimkan semua hasil perhitungan ke browser dalam format JSON.

##### Baris 60-61
<img width="491" height="71" alt="image" src="https://github.com/user-attachments/assets/a145a731-7a9e-43bb-b313-e3104fbc740e" />
Menjalankan server Flask secara lokal. debug=True membuat server otomatis restart saat kode diubah.








  
  











