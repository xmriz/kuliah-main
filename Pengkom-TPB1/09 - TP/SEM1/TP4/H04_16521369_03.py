# NIM/NAMA    : 16521369_Ahmad Rizki
# Tanggal     : 14 Oktober 2021
# Deskripsi   : Program yang menerima input N,dan menuliskan matriks segitiga pascal berukuran N x N

# KAMUS
# N : int
# Mat : matriks of int

# ALGORITMA

# menginput nilai N
N = int(input('Masukkan N: '))

# inisialisasi matriks dengan ukuran N x N, dan menuliskan 1 sebagai nilai defaultnya
Mat = [[1 for j in range(N)] for i in range (N)]

# mengisi matriks, dimana merupakan penjumlahan antara bilangan di kiri dan di atas
for i in range(1, N):
    for j in range(1, N):
        Mat[i][j] = Mat[i-1][j] + Mat[i][j-1]

# mencetak matriks yang telah di isi
for i in range(N):
    for j in range(N):
        print(Mat[i][j], end= ' ')
    print()