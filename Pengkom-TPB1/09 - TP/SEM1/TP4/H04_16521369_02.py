# NIM/NAMA    : 16521369_Ahmad Rizki
# Tanggal     : 14 Oktober 2021
# Deskripsi   : Program yang menerima input N dan M, lalu membaca matriks A berukuran N x M, serta menuliskan banyak bilangan positif pada matriks serta menuliskan isi matriks itu sendiri

# KAMUS
# N, M: int
# A : matriks of int

# ALGORITMA

# melakukan input N dan M, dengan asumsi bilangan bulat
N = int(input('Masukkan N: '))
M = int(input('Masukkan M: '))

# inisialisasi matriks A, dengan ukuran N x M
A = [[0 for j in range(M)] for i in range(N)]

# inisialisasi banyak bilangan positif awal adalah 0
Positif = 0

# melakukan perulangan untuk mengisi matriks, dan mengecek apakah bilangan positif
for i in range(N):
    for j in range(M):
        A[i][j] = int(input(f'Masukkan nilai A[{i+1}][{j+1}]: '))
        if A[i][j] > 0:
            Positif += 1

# mencetak banyak bilangan positif dan isi dari matriks
print(f'Ada {Positif} bilangan positif di matriks')
for i in range(N):
    for j in range(M):
        print(A[i][j], end=' ')
    print()