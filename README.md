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
- 
###### maka hasilnya:
- ROP        = (50 × 7) + 100 = 450 pcs
- Stok habis = 200 ÷ 50       = 4 hari lagi
- Status     = 🔴 BAHAYA — stok sudah di bawah ROP, order sekarang!

# Simulasi Penggunaaan
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


# Penjelasan APP.PY 
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


# Penjelasan index.html

##### Baris 1-8
<img width="1101" height="259" alt="image" src="https://github.com/user-attachments/assets/ca0ddc24-e516-4f9d-b60b-ac247edd25e5" />

- lang="id" = mendeklarasikan bahasa halaman adalah Indonesia.
- meta viewport = tampilan responsif di layar HP
- url_for(...) = sintaks Flask untuk menghasilkan path yang benar ke file CSS

##### Baris 13-43
<img width="771" height="644" alt="image" src="https://github.com/user-attachments/assets/75d5f5a5-adad-4595-94ba-ed89a82a01ee" />

Bagian layar kalkulator mulai dari atas form atau judulnya sampai kartu kalkulatornya. 

Awalnya menampilkan —. Setelah HITUNG diklik, JavaScript mengubah isinya dengan hasil ROP. ID digunakan JavaScript untuk menemukan dan mengupdate elemen ini. juga ada tampilan untuk kalkulatornya, layar hasil dan sedikit penjelasan.
<img width="564" height="305" alt="image" src="https://github.com/user-attachments/assets/1f177be2-ca6c-43ca-8040-6452069d602c" />

##### Baris 45-84
<img width="822" height="809" alt="image" src="https://github.com/user-attachments/assets/60cb9fef-886b-4b35-bb42-5959239b8953" />

menampilkan layar kalkulator juga. perhitungannya saat mengisi output variabelnya sehingga nanti bisa dihitung.

<img width="439" height="188" alt="image" src="https://github.com/user-attachments/assets/303eb6b8-fca0-4455-b708-ccbd5bbdcd7e" />

##### Baris 86-134
<img width="624" height="832" alt="image" src="https://github.com/user-attachments/assets/99286a8f-becd-4cb2-9a5f-9de2463274c6" />

- **Bagian HASIL**
  
Baris 87 = Kotak hasil awalnya disembunyikan. display:none artinya tidak kelihatan dulu baru muncul setelah user klik HITUNG, diatur lewat JavaScript.

Baris 90 = Tempat menampilkan angka hasil ROP. Awalnya isi "—", nanti diisi angka oleh JavaScript. id="r-reorder" dipakai JavaScript untuk menemukan elemen ini.

Baris 92-103 = Sama seperti di atas. masing-masing tempat untuk menampilkan: stok habis dalam berapa hari, kapan harus order, dan stok cadangan. Warnanya berbeda: hijau = positif, amber = peringatan, rose = perlu perhatian.

- **Bagian VISUALISASI BAR STOK**

Baris 106-110 = Label di atas bar. menunjukkan 3 titik: kiri = habis, tengah = titik ROP, kanan = posisi stok sekarang.

Baris 112-116 = Bar warna-warni yang dibagi 3 zona: merah = bahaya, kuning = waspada, hijau = aman. Lebarnya diatur JavaScript berdasarkan perbandingan stok sekarang dengan ROP.

Baris 1171-122 = Label di bawah bar. keterangan tiap zona warna.

- **Bagian STATUS BADGE**

Baris 124-125 = Kotak status yang muncul setelah hitung. isinya teks seperti "Stok aman" atau "Stok kritis!". Isi dan warnanya diubah JavaScript sesuai hasil perhitungan.

- **Bagian TOMBOL**
  
Baris 127-134 = Dua tombol utama. onclick="hitung()" artinya saat diklik, jalankan fungsi hitung() di JavaScript. onclick="reset()" artinya jalankan fungsi reset() yang mengosongkan semua input dan menyembunyikan hasil.

<img width="538" height="339" alt="image" src="https://github.com/user-attachments/assets/a2594496-c083-479f-adca-39c3afae19d6" />

##### Baris 136-168

<img width="618" height="563" alt="image" src="https://github.com/user-attachments/assets/4260d400-3a87-4e89-8790-889e47c3f8b8" />
<img width="518" height="198" alt="image" src="https://github.com/user-attachments/assets/47c86b6c-fb62-49a0-aa14-8413b61aa124" />

untuk menampilkan sebuah panel toggle berisi informasi tentang seorang pembuat websitenya. 
juga di **baris 252** itu untuk Membuka/menutup panel "Tentang website ini". Ikon panah ikut berganti arah.

<img width="602" height="358" alt="image" src="https://github.com/user-attachments/assets/0cacd998-d777-4da1-a7d0-39f0ab9592fc" />

##### Baris 170-239

<img width="501" height="804" alt="image" src="https://github.com/user-attachments/assets/0b3b0e12-8d6e-4f58-b394-21826f927ec6" />

Baris 172 = Mengubah angka menjadi format ribuan Indonesia saat pengguna mengetik.

Baris 178 = Membaca nilai input yang sudah diformat dan mengembalikannya sebagai angka murni. Contoh: mengambil "25.000" dari field, mengembalikan 25000.

Baris 197 = async/await = fungsi asinkron agar halaman tidak membeku saat menunggu respons server
fetch('/hitung', {...}) = mengirim data ke Flask tanpa reload halaman
JSON.stringify(payload) = mengubah objek JavaScript menjadi string JSON
if (data.error) = jika server mengembalikan error, tampilkan alert

Baris 183 = Menghitung dan mengatur lebar tiap zona bar secara proporsional berdasarkan nilai ROP.

##### Baris 241-250

<img width="408" height="145" alt="image" src="https://github.com/user-attachments/assets/9fe0568e-7b00-4bbe-86b9-e99544241244" />

Menghapus semua input dan menyembunyikan area hasil kembali ke kondisi awal.


# Simulasi Uji Coba

### **1. Input Diisi angka 0 semua**

<img width="809" height="811" alt="image" src="https://github.com/user-attachments/assets/c3a55776-5b63-475e-928d-a06b3f3f25ed" />

Yang terjadi: Validasi di app.py menangkap kondisi ini sebelum kalkulasi dijalankan.

<img width="643" height="107" alt="image" src="https://github.com/user-attachments/assets/4e640659-5c22-4b63-ba6d-3d3df9be0882" />
    
Hasil: Browser menampilkan pop-up alert dengan pesan error. Kalkulasi tidak dijalankan.

### **2. Uji Coba Mengganti Nama Variabel**

Misalnya variabel **Reorder Point** diganti menjadi **titik_order**:

###### Sebelum

<img width="619" height="701" alt="image" src="https://github.com/user-attachments/assets/f083812f-803c-410d-a01c-a00363d9cdc4" />

###### Sesudah

<img width="621" height="648" alt="image" src="https://github.com/user-attachments/assets/806b5416-eaf7-4d10-8ba7-6c6168eae595" />

### simulasi menghitung ketika variabelnya diganti:

**misal jika saya tidak mengganti semua variabelnya atau ada yang missing atau tidak konsisten mengisinya maka hasilnya akan seperti ini:**

<img width="420" height="631" alt="image" src="https://github.com/user-attachments/assets/f343867f-fe3e-42f1-bf58-41b729cbcc68" />

**keterangan:**

angka pada hasil perhitungannya tidak muncul, karena masih ada variabel baris reorder point sebelumnya **(contoh pada baris 231 dibawah)** yang di dipanggil sehingga eror.

<img width="641" height="424" alt="image" src="https://github.com/user-attachments/assets/889987f4-f9c5-40c7-82a1-48b8900379d1" />

- nah, ketika saya sudah konsisten mengganti semua variabel dari **reorder point** ke **titik_order**, maka hasil kalkulatornya berjalan denagn baik, seperti gambar di bawah:

<img width="408" height="645" alt="image" src="https://github.com/user-attachments/assets/ce86eaf5-05e2-4f98-ad27-4a279f4927a7" />

**Contoh Yang terjadi:**

- Diganti hanya di satu baris = aplikasi error karena variabel reorder_point masih dipanggil di baris lain
- Diganti konsisten di semua baris = aplikasi tetap berjalan normal
- Nama variabel boleh diganti asal konsisten di semua baris yang menggunakannya
----------------------------------------------------------------------------------------------------------------------------------------------------------
### Cara menjalankan

#### 1. Install Flask
pip install flask

#### 2. Jalankan server
python app.py

#### 3. Buka browser
####  http://127.0.0.1:5000

## TERIMA KASIH





  
  











