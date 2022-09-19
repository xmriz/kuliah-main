# NIM/NAMA    : 16521369_Ahmad Rizki
# Tanggal     : 5 Oktober 2021
# Deskripsi   : Program yang menentukan apakah sebuah bilangan positif genap, positif ganjil, negatif, atau nol.

# KAMUS
# X : integer

# Melakukan input bilangan yang akan ditentukan
X = int(input('Masukkan X: '))

# Melakukan percabangan sesuai jenis bilagan yang ditentukan
if X > 0:
    if X % 2 == 0: # Untuk X positif, lakukan percabangan untuk postif ganjil dan juga positif genap   
        print('X adalah bilangan positif genap')
    else:
        print('X adalah bilangan positif ganjil')
elif X == 0:
    print('X adalah bilangan nol')
else:
    print('X adalah bilangan negatif')

        