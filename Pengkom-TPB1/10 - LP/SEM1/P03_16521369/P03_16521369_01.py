# NIM/NAMA  : 16521369/Ahmad Rizki
# Tanggal   : 3 November 2021
# Deskripsi : Program menentukan banyaknya hari maksimal untuk Tuan Dip menonton TV

# KAMUS
# N, k, jumlah_koin, h : int
# koin_hari : array of int

# ALGORITMA

# menginput jumlah hari menonton dan jumlah koin TUan Dip
N = int(input('Masukkan jumlah hari (N): '))
k = int(input('Masukkan jumlah koin Tuan Dip (k): '))

# deklarasi array untuk list daftar harga
koin_hari = [0 for i in range(N)]

# deklarasi jumlah koin awal yang digunakan 
jumlah_koin = 0

# banyak hari
h = 0

# megisi array daftar harga untuk menonton
for i in range(N):
    koin_hari[i] = int(input(f'Biaya hari ke {i+1}: '))

# mencari nilai minimum dari daftar, dengan mendeklarasikan nilai terkecil awal adalah index ke-0 pada daftar
while jumlah_koin < k:
    min = koin_hari[0]
    for i in range(len(koin_hari)):
        if koin_hari[i] < min:
            min = koin_hari[i]
    jumlah_koin += min
    koin_hari.remove(min)
    h += 1

print(f'Maksimalnya adalah {h-1} hari')







