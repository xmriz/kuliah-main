# NIM/NAMA    : 16521369_Ahmad Rizki
# Tanggal     : 29 Oktober 2021
# Deskripsi   : Program mengecek apakah Y merupakan tahun kabisat atau bukan

# KAMUS
# Y : int

# ALGORITMA

# menginput nilai Y sebagai tahun
Y = int(input('Masukkan tahun: '))

# membuat percabangan mengenai aturan kabisat
if Y > 0:
    if Y % 4 == 0:
        if Y % 100 == 0:
            if Y % 400 == 0:
                print('tahun kabisat')
            else:
                print('bukan tahun kabisat')
        else:
            print('tahun kabisat')
    else:
        print('bukan tahun kabisat')
else:
    print('masukan salah')