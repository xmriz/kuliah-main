# NIM/NAMA  : 16521369/Ahmad Rizki
# Tanggal   : 17 November 2021
# Deskripsi : Program menentukan mahasiswa ke berapa yang mempunyai nilai rata-rata tertinggi

# KAMUS
# 


# definisi fungsi enskrip 
def avg(i, M):
    # fungsi untuk menghitung rata dari baris matriks (tiap mahasiswa)

    # KAMUS LOKAL
    # jumlah, i, M, rata2 : int

    # ALGORTIMA
    jumlah = 0
    for a in range(M):
        jumlah += data[i][a]
    rata2 = jumlah/M
    return rata2


# ALGORITMA UTAMA

# input N dan M
N = int(input('Masukkan banyak Mahasiswa (N): '))
M = int(input('Masukkan banyak ujian (M): '))

# inisialisasi matriks data, dimana baris menunjukkan banyak mahasiswa, dan kolom menunjukkan nilai (N x M)
data = [[0 for j in range(M)] for i in range(N)]

# mengisi matriks data
for i in range(N):
    for j in range(M):
        data[i][j] = int(input(f'Masukkan nilai Ujian ke {j+1} mahasiswa {i+1}: '))

# inisialisasi array untuk rata-rata nilai dari tiap mahasiswa
array = [0 for i in range(N)]

# Mengisi array rata-rata
for i in range(N):
    array[i] = avg(i, M)

# inisialisasi nilai rata2 maximum
max = 0

# mengecek rata-rata tertinggi
for i in range(N):
    if array[i] > max:
        max = array[i]

# mencetak mahasiswa yang memiliki nilai rata2 tertinggi
print('Mahasiswa dengan rata-rata tertinggi adalah mahasiswa', end= ' ')
for i in range(N):
    if array[i] == max:
        print(f'{i+1}', end=' ')