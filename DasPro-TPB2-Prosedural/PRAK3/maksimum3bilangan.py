# NIM/Nama	: 16521369/Ahmad Rizki
# Nama file	: maksimum3bilangan.py
# Topik		: Review Prosedural dengan Bahasa Python
# Tanggal	: 2 Maret 2022
# Deskripsi	: program yang membaca 3 buah bilangan integer dan menuliskan nilai terbesar di antara ketiganya.

# KAMUS
# a, b, c : int 

# ALGORITMA
# input
a = int(input())
b = int(input())
c = int(input())

# inisialisasi
max = a

# percabangan
if b > max:
    max = b
if c > max:
    max = c

# output
print(max)
