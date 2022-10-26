import numpy as np
import matplotlib.pyplot as plt
import math
from os import system
from tabulate import tabulate


def f(x):
    """Fungsi yang akan dicari akarnya"""
    return math.e**(-x)-x


def is_valid(a, b, error_tol):
    """Mengecek validitas interval untuk dijadikan batas pencarian akar"""
    curr_error = abs(a - b)
    if curr_error < error_tol:
        return False
    if f(a) * f(b) > 0:
        return False
    return True


# Inisialisasi
low_lim = 0  # batas bawah
up_lim = 1  # batas atas
scale = 5  # jumlah digit di belakang koma
max_iter = 10  # jumlah iterasi maksimum
error_tol = 0.0001  # toleransi eror
iter, x1, x2, x3, f_x1, f_x2, f_x3, error = [], [], [], [], [
], [], [], []  # inisialisasi list untuk menyimpan data

# Initial error handling
try:
    assert is_valid(low_lim, up_lim, error_tol)
except AssertionError:
    print("Eror: tidak ditemukan akar pada interval ini. Masukkan interval lain.")
    system("pause")
    exit()

# Pencarian akar
termin_flag = False
for i in range(max_iter):

    if is_valid(low_lim, up_lim, error_tol):
        # Mencari titik tengah
        med = (low_lim + up_lim) / 2

        # Menyimpan data
        iter.append(i+1)
        x1.append(low_lim)
        x2.append(up_lim)
        x3.append(med)
        f_x1.append(f(low_lim))
        f_x2.append(f(up_lim))
        f_x3.append(f(med))
        error.append(abs(low_lim - up_lim))

        # Mencari batas atas atau bawah yang baru
        if f(low_lim) * f(med) > 0:
            low_lim = med
        else:
            up_lim = med

    else:
        termin_flag = True
        break

# Tabel hasil
data = {
    'Iterasi': iter,
    'x1': [round(i, scale) for i in x1],
    'x2': [round(i, scale) for i in x2],
    'x3': [round(i, scale) for i in x3],
    'f(x1)': [round(i, scale) for i in f_x1],
    'f(x2)': [round(i, scale) for i in f_x2],
    'f(x3)': [round(i, scale) for i in f_x3],
    'Eror': [round(i, scale) for i in error]
}
print(tabulate(data, headers='keys', tablefmt='fancy_grid'))
print('Ditemukan aproksimasi akar terdekat:', round(x3[-1], scale))

if termin_flag:
    print('NB: proses diterminasi pada iterasi ke-' +
          str(iter[-1]) + ' karena telah mencapai batas maksimum toleransi eror.')

# Plot
fig, ax = plt.subplots()

x = np.linspace(-10, 10, 2100)
ax.plot(x, np.zeros_like(x), 'k')  # grafik sumbu x
ax.plot(np.zeros_like(x), x, 'k')  # grafik sumbu y
ax.plot(x, f(x))  # grafik fungsi

ax.plot(x3, f_x3, 'yo', label='Aproksimasi Akar')
ax.plot(x3[-1], f_x3[-1], 'go', label='Aproksimasi Terdekat')

ax.set(title='Grafik Metode Bolzano untuk f(x) = e^(-x)-x',
       xlabel='x', ylabel='f(x)')
ax.legend()
ax.grid()

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()
