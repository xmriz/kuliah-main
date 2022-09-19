# NIM/NAMA    : 16521369_Ahmad Rizki
# Tanggal     : 18 Oktober 2021
# Deskripsi   : Program yang menerima bilangan dan mengecek apakah bilangan tersebut adalah bilangan prima atau tidak

# KAMUS
# X : integer
# counter : 0

# ALGORITMA
# Menginput nilai X, dimana X adalah bilangan bulat lebih besar dari 0
X = int(input('Masukkan X: '))

# Mendefinisikan nilai awal dari counter sebgai 0
counter = 0

# Melakukan perulangan untuk pembagian X dengan bilangan dari 1 sampai dengan X
for i in range(1, X+1):
    if X % i == 0:
        counter += 1

# Melakukan percabangan, sesuai definisi bilangan prima (bilangan yang dapat habis dibagi dengan 1 dan dirinya sendiri), sehingga jika operasi pembagian yang bersisa 0 berjumlah dua artinya X adalah bilangan prima
if counter == 2:
    print(f'{X} adalah bilangan prima')
else:
    print(f'{X} bukan bilangan prima')
