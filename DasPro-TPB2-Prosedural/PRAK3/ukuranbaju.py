# NIM/Nama	: 16521369/Ahmad Rizki
# Nama file	: ukuranbaju.py
# Topik		: Review Prosedural dengan Bahasa Python
# Tanggal	: 2 Maret 2022
# Deskripsi	: program yang membaca masukan 2 buah integer positif, misalnya t (tinggi badan dalam cm) dan b (berat badan dalam kg) 
#             dan menuliskan kode ukuran baju (1 adalah M, 2 adalah L, 3 adalah XL) atau kode 4 adalah untuk yang tidak mendapatkan kaos.

# KAMUS
# t, b : integer


# ALGORITMA

# input tinggi dan berat
t = int(input())
b = int(input())

# percabangan
if t <= 150:
    print(1)
elif (150 < t <= 170):
    if b <= 80:
        print(2)
    else:
        print(3)
elif t > 170 and (60 < b <= 80):
    print(3)
else:
    print(4)    

