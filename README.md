# TipeData_Dictionary__PY

Bahan Ajar Fundamental Pemrograman Python. Mengenal Tipe Data Dictionary Beserta Cara Menggunakan dan Mengakses Data di dalamnya.<br><br>
<img src="https://github.com/RizkyKhapidsyah/TipeData_Dictionary__PY/blob/master/result/001.PNG"><br><br>
- Lihat <a href="https://github.com/RizkyKhapidsyah/TipeData_Dictionary__PY/blob/master/TipeData_Dictionary__PY.py">Source Code.</a><br><br>


# Pengertian Tipe Data Dictionary Python

Tipe data dictionary adalah tipe data array dimana key atau index dari array bisa berbentuk string, tidak hanya number saja. Dalam bahasa pemrograman lain (seperti PHP) dictionary ini dikenal juga dengan sebutan associative array.

Dictionary Python berbeda dengan List ataupun Tuple. Karena setiap urutanya berisi key dan value. Setiap key dipisahkan dari value-nya oleh titik dua (:), item dipisahkan oleh koma, dan semuanya tertutup dalam kurung kurawal. Dictionary kosong tanpa barang ditulis hanya dengan dua kurung kurawal, seperti ini: {}. Nilai kamus bisa berupa tipe apa pun, namun key harus berupa tipe data yang tidak berubah seperti string, angka, atau tupel.

Berikut format dasar penulisan dictionary dalam bahasa Python:

      nama_variabel = { "key1": "value1", "key2": "value2", "key3": "value3" }

Tipe data dictionary ini cocok dipakai untuk kelompok data yang kompleks (terdiri dari banyak element).

# Cara Pembuatan Tipe Data Dictionary Python

Dalam pembuatan dictionary, kita menggunakan tanda kurung kurawal { dan } . Selain itu setiap element merupakan pasangan dari key dan value. Antar satu element dengan element lain dipisah dengan tanda koma seperti contoh berikut:

      foo = { 1: "Belajar", 2: "Python", 3: "di rikymetalist.blogspot.com" }
      bar = { "mengapa": "Belajar", "apa": "Python", "dimana": "di rikymetalist.blogspot.com" }
      baz = { 1: "Belajar", "apa": "Python", "dimana": "di rikymetalist.blogspot.com" }

      print(type(foo))
      print(type(bar))
      print(type(baz))

      print(foo)
      print(bar)
      print(baz)

Di sini saya membuat 3 buah variabel: foo, bar dan baz yang masing-masingnya diisi dengan tipe data dictionary. Untuk variabel foo saya isi dengan dictionary dimana semua key-nya berupa angka (1, 2 dan 3). Jika ditulis seperti ini, foo mirip seperti tipe data list.

Untuk variabel bar saya isi dengan semua key berbentuk string (“mengapa”, “apa”, dan “dimana”). Terakhir untuk variabel baz mengkombinasikan penulisan key antara number dan string (1, “apa”, dan “dimana”). Perintah di baris 5 – 7 membuktikan bahwa ketiga variabel bertipe dict (singkatan dari dictionary). Untuk menampilkan seluruh isi dictionary, kita bisa memakai perintah print seperti di baris 9 – 11.

Nilai atau value dari setiap element dictionary bisa terdiri dari berbagai tipe data:

      foo = { 1: "Belajar", 
              2: ["Pascal", "C", "Python"],
              "website": "rikymetalist.blogspot.com",
              "menyerah" : False,
              "target": 2020,
              "riwayat_sekolah": {
                "SD": "SDN 3 Hijau Daun",
                "SMP": "SMP 7 Hijau Lumut",
                "SMA": "SMA 8 Hijau Rumput"}
            }

      print(foo)

Sekarang variabel foo saya isi dengan 6 element dictionary dengan tipe data yang berbeda-beda, mulai dari string, boolean, number, list, hingga dictionary lain.

# Cara Mengakses Element Dictionary Python

Untuk mengakses elemen Dictionary, Anda dapat menggunakan tanda kurung siku yang sudah dikenal bersama dengan key untuk mendapatkan nilainya. Berikut adalah contoh sederhananya :

      dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
      print ("dict['Name']: ", dict['Name'])
      print ("dict['Age']: ", dict['Age'])

Untuk menampilkan satu element yang ada di dalam dictionary, tulis key atau index yang ingin diakses dalam kurung siku:

      foo = { "kegiatan": "Belajar Python",
              "website": "rikymetalist.blogspot.com",
              "hasil": "Yakin bisa!" }

      print(foo["website"])

# Cara Mengubah Element Dictionary Python

Setelah di deklarasikan, kita bisa mengubah nilai dari sebuah element dictionary. Caranya mirip seperti tipe data list, yakni mengisi nilai ke dalam key atau index dictionary:

      foo = { "kegiatan": "Belajar Python",
              "website": "rikymetalist.blogspot.com",
              "hasil": "Yakin bisa!" }

      foo["kegiatan"] = "Belajar Bahasa Pemrograman"
      print(foo)

# Cara Menambah Element Dictionary Python

Anda dapat memperbarui Dictionary dengan menambahkan entri baru atau pasangan nilai kunci, memodifikasi entri yang ada, atau menghapus entri yang ada seperti ditunjukkan pada contoh sederhana yang diberikan di bawah ini.

      dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
      dict['Age'] = 8; # Mengubah entri yang sudah ada
      dict['School'] = "DPS School" # Menambah entri baru

      print ("dict['Age']: ", dict['Age'])
      print ("dict['School']: ", dict['School'])

Untuk menambah element baru ke dalam dictionary, bisa dilakukan dengan cara mengisi nilai ke sebuah key baru:

      foo = { "kegiatan": "Belajar Python",
              "website": "rikymetalist.blogspot.com",
              "hasil": "Yakin bisa!" }

      foo["target"] = 2020
      print(foo)

# Cara Menghapus Element Dictionary Python

Untuk menghapus element dari sebuah dictionary, bsia menggunakan perintah del. Berikut contohnya:

      foo = { "kegiatan": "Belajar Python",
              "website": "rikymetalist.blogspot.com",
              "hasil": "Yakin bisa!" }

      del foo["kegiatan"]
      print(foo)
      
Anda dapat menghapus elemen Dictionary individual atau menghapus keseluruhan isi Dictionary. Anda juga dapat menghapus seluruh Dictionary dalam satu operasi. Untuk menghapus seluruh Dictionary secara eksplisit, cukup gunakan del statement. Berikut adalah contoh sederhana :

      dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

      del dict['Name'] # hapus entri dengan key 'Name'
      dict.clear()     # hapus semua entri di dict
      del dict         # hapus dictionary yang sudah ada

      print ("dict['Age']: ", dict['Age'])
      print ("dict['School']: ", dict['School'])
 
# Pembuatan Dictionary dengan constructor <code>dict()</code> 

Selain menggunakan tanda kurung kurawal, proses pembuatan dictionary di dalam bahasa Python juga bisa dilakukan menggunakan “constructor” <code>dict()</code>:

      foo = dict ( kegiatan = "Belajar Python",
                   website = "rikymetalist.blogspot.com",
                   hasil = "Yakin bisa!" )

      print(foo)

Dengan menggunakan perintah <code>dict()</code>, kita tidak lagi memakai tanda kurung kurawal, tapi cukup tanda kurung biasa. Selain itu key element juga tidak perlu menggunakan tanda kutip, dan tanda sama dengan <code>‘=’</code>  dipakai untuk menginput nilai ke dalam element dictionary. Ini hanya alternatif penulisan, anda bebas ingin menggunakan cara biasa dengan tanda kurung kurawal, atau menggunakan constructor <code>dict()</code> untuk membuat tipe data dictionary.

# Fungsi Build-in Pada Dictionary Python

Python menyertakan fungsi built-in sebagai berikut :


<table>
  <thead>
    <tr>
      <th>Fungsi Python</th>
      <th>Penjelasan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>cmp(dict1, dict2)</td>
      <td>Membandingkan unsur keduanya.</td>
    </tr>
    <tr>
      <td>len(dict)</td>
      <td>Memberikan panjang total Dictionary. Ini sama dengan jumlah item dalam Dictionary.</td>
    </tr>
    <tr>
      <td>str(dict)</td>
      <td>Menghasilkan representasi string yang dapat dicetak dari Dictionary</td>
    </tr>
    <tr>
      <td>type(variable)</td>
      <td>Mengembalikan tipe variabel yang lulus. Jika variabel yang dilewatkan adalah Dictionary, maka akan mengembalikan tipe Dictionary.</td>
    </tr>
  </tbody>
</table>

---

<table>
  <thead>
    <tr>
      <th>Method Python</th>
      <th>Penjelasan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>dict.clear()</td>
      <td>Menghapus semua elemen Dictionary</td>
    </tr>
    <tr>
      <td>dict.copy()</td>
      <td>Mengembalikan salinan Dictionary</td>
    </tr>
    <tr>
      <td>dict.fromkeys()</td>
      <td>Buat Dictionary baru dengan kunci dari seq dan nilai yang disetel ke nilai.</td>
    </tr>
    <tr>
      <td>dict.get(key, default=None)</td>
      <td>For key, nilai pengembalian atau default jika tombol tidak ada dalam Dictionary</td>
    </tr>
    <tr>
      <td>dict.has_key(key)</td>
      <td>Mengembalikan true jika key dalam Dictionary, false sebaliknya</td>
    </tr>
    <tr>
      <td>dict.items()</td>
      <td>Mengembalikan daftari dari pasangan tuple dictionary (key, value)</td>
    </tr>
    <tr>
      <td>dict.keys()</td>
      <td>Mengembalikan daftar key dictionary</td>
    </tr>
    <tr>
      <td>dict.setdefault(key, default=None)</td>
      <td>Mirip dengan get (), tapi akan mengatur dict [key] = default jika kunci belum ada di dict</td>
    </tr>
    <tr>
      <td>dict.update(dict2)</td>
      <td>Menambahkan pasangan kunci kata kunci dict2 ke dict</td>
    </tr>
    <tr>
      <td>dict.values()</td>
      <td>Mengembalikan daftar nilai dictionary</td>
    </tr>
  </tbody>
</table>


-----
<font size="1">Referensi Artikel:</font> <a href="https://www.duniailkom.com">DuniaIlkom</a>, <a href="https://belajarpython.com">BelajarPython</a>. Thanks To: <a href="https://www.duniailkom.com">DuniaIlkom</a>, <a href="https://belajarpython.com">BelajarPython</a><br>
Referensi Source Code: <a href="https://www.youtube.com/user/faqihzamukhlish"> Kelas Terbuka </a> dan <a href="https://github.com/kelasterbuka"> Kelas Terbuka (Repository)</a>. Created by <a href="https://github.com/faqihza">Faqihza Mukhlish.</a> Thanks To: <a href="https://www.youtube.com/channel/UCRGHjysoCemh4y7tCJQs30w/about">Faqihza Mukhlish.</a><br>


-----
All Source Code is Modified.
