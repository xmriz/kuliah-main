# NIM/NAMA  : 16521369/Ahmad Rizki
# Tanggal   : 12 Oktober 2021
# Deskripsi : program mencari deret aritmatika suku ke-n

# KAMUS
# lebar_dada : int

# Melakukan input lebar dada dalam cm, dengan asumsi lebar dada selalu lebih besar dari 0
lebar_dada = int(input('Masukkan lebar dada (dalam cm): '))

# Melakukan percabangan untuk tiap jenis ukuran, lalu mencetak ukuran yang cukup
if lebar_dada <= 46:
    print('Ukuran kaos yang cukup adalah S')
elif 46 < lebar_dada <= 48:
    print('Ukuran kaos yang cukup adalah M')
elif 48 < lebar_dada <= 50:
    print('Ukuran kaos yang cukup adalah L')
elif 50 < lebar_dada <= 52:
    print('Ukuran kaos yang cukup adalah XL')
elif 52 < lebar_dada <= 54:
    print('Ukuran kaos yang cukup adalah XXL')
else:
    print('Tidak ada ukuran kaos yang cukup')