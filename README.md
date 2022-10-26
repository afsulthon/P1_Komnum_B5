# P1_Komnum_B5

**Praktikum 1 Komputasi Numerik**  
**Kelas Komputasi Numerik (B)**

**Kelompok 5**
1. Akmal Sulthon Fathulloh (5025211047)
2. Thariq Agfi Hermawan (5025211215)
3. Tigo S Yoga (5025211125)

## Penjelasan Singkat Metode Bolzano

Metode Bolzano, dikenal pula dengan metode setengah interval (*interval halving*), metode bagi dua, metode biseksi, atau metode pemotongan biner, merupakan metode pencarian akar suatu persamaan yang membagi suatu interval menjadi 2 bagian kemudian memilih interval mana yang seharusnya mengapit akar untuk diproses lebih lanjut. Metode ini sangat sederhana, tetapi juga sangat lambat.

Langkah yang terlebih dahulu dilakukan adalah menginisialisasi 2 titik awal, sebut saja `a` dan `b`, sedemikian sehingga `f(a)` dan `f(b)` harus berlainan tanda. Menurut [*intermediate value theorem*](https://en.wikipedia.org/wiki/Intermediate_value_theorem), fungsi `f` pasti memiliki setidaknya 1 akar dalam interval 2 titik (dalam kasus ini `(a, b)`) yang berlainan tanda. Langkah selanjutnya adalah mencari titik tengah kedua titik `a` dan `b`, sebut saja `c`. Sekarang, ada 2 kemungkinan: `f(a)` dan `f(c)` memiliki tanda berlawanan dan mengapit akar, atau `f(b)` dan `f(c)` memiliki tanda berlawanan dan mengapit akar. Kita pilih interval mana yang mengapit akar dan menerapkan algoritma serupa terhadapnya. Dengan demikian, interval yang mungkin mengapit akar akan dikurangi lebarnya 50% setiap iterasi sehingga setelah iterasi yang cukup banyak akan didapatkan interval yang cukup kecil.

## Implementasi Metode Bolzano pada Program Python

Pertama, melakukan inisialisasi beberapa data, yaitu:
- `low_lim` -> lower limit (batas bawah)
- `up_lim` -> upper limit (batas atas)
- `scale` -> jumlah digit angka di belakang koma
- `max_iter` -> jumlah iterasi maksimum
- `error_tol` -> toleransi eror

Setelah diinisialisasi, dilakukan pengecekan awal apakah data interval yang diinput sudah valid (ada akar yang diapit oleh kedua batas).
```py
try:
    assert is_valid(low_lim, up_lim, error_tol)
except AssertionError:
    print("Eror: tidak ditemukan akar pada interval ini. Masukkan interval lain.")
    exit()
```
Program akan diterminasi jika input invalid. Jika input valid, maka dilanjutkan proses iterasi. Proses iterasi dilakukan sebanyak `max_iter` selama kondisi masih valid. Berikut adalah fungsi validasinya.
```py
def is_valid(a, b, error_tol):
    curr_error = abs(a - b)
    if curr_error < error_tol:
        return False
    if f(a) * f(b) > 0:
        return False
    return True
```
Kondisi dianggap valid jika dan hanya jika `f(a)` dan `f(b)` berlainan tanda (plus-minus atau minus-plus), serta `curr_error` (eror saat ini) masih di atas `error_tol`. `curr_error` dicari dengan menghitung selisih mutlak antara `a` dan `b` dengan asumsi kita tidak mengetahui nilai akar yang pasti dari persamaan sebelumnya.

Dalam setiap iterasi, dilakukan penghitungan nilai tengah dari `low_lim` dan `up_lim` yang disimpan dalam variabel `med`. Selanjutnya dilakukan pengisian secara berturut-turut nilai `i+1`, `low_lim`, `up_lim`, `med`, `f(low_lim)`, `f(up_lim)`, `f(med)`, dan `abs(x1-x2)` ke list tabel hasil `iter`, `x1`, `x2`, `x3`, `f_x1`, `f_x2`, `f_x3`, dan `error` untuk diolah lebih lanjut.

Jika `f(low_lim)` dan `f(med)` memiliki tanda berlawanan, maka akar berada di interval `(low_lim, med)` sehingga nilai `med` akan disimpan sebagai `up_lim` untuk iterasi selanjutnya. Sebaliknya, jika `f(up_lim)` dan `f(med)` memiliki tanda berlawanan, maka akar berada di interval `(med, up_lim)` sehingga nilai `med` akan disimpan sebagai `low_lim` untuk iterasi selanjutnya.

Hal ini akan terus dilakukan selama kondisi masih valid. Jika `curr_error` sudah di bawah `error_tol`, maka iterasi akan berhenti dan nilai `termin_flag` akan diset menjadi `True`. `termin_flag` berfungsi untuk memberitahukan bahwa iterasi diterminasi sebelum mencapai `max_iter` dan memunculkan pesan pemberitahuan.

```py
if termin_flag:
    print('NB: proses diterminasi pada iterasi ke-' +
          str(iter[-1]) + ' karena telah mencapai batas maksimum toleransi eror.')
```

Setelah semua proses selesai, semua data pada tabel lalu dicetak di terminal dan grafik fungsi beserta titik akar (`x3`) diplotkan pada jendela *matplotlib*.

## Hasil Implementasi

Berikut adalah hasil keluaran program untuk persamaan `f(x) = e^(-x) - x` dengan batas bawah `low_lim = 0`, batas atas `up_lim = 1`, digit di belakang koma `scale = 5`, jumlah iterasi maksimum `max_iter = 10`, dan toleransi eror `error_tol = 0.0001`.

Plot grafik:  
<img src="https://i.imgur.com/Gnsda8U.png" alt="Grafik" width="500"/>

Tabel data:  
<img src="https://i.imgur.com/XsMaFVk.png" alt="Tabel Data" width="500"/>

Berikut adalah contoh ketika program diterminasi karena tidak ditemukan akar pada interval yang diinput.
<img src="https://i.imgur.com/vgKUuhW.png" alt="Tabel Data" width="500"/>

Berikut adalah contoh ketika program diterminasi karena telah mencapai batas maksimum toleransi eror.  
<img src="https://i.imgur.com/IniSsaG.png" alt="Selesai" width="500"/>

## Dependensi
Dependensi yang diperlukan untuk menjalankan program ini adalah:
- `numpy`
- `matplotlib`
- `tabulate`