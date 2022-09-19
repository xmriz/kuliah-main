# NIM/NAMA    : 16521369_Ahmad Rizki
# Tanggal     : 16 Oktober 2021
# Deskripsi   : Program yang mengecek apakah sebuah string palindrom

# KAMUS
# l : int
# string : str (array of char)
# ispalindrom : bool

# ALGORITMA

# menginput panjang string, dengan asumsi panjang string selalu sama dengan panjang string sebenarnya
l = int(input('Masukkan panjang string: '))

# menginput string
string = input('Masukkan string: ')

# deklarasi asumsi awal string adalah palindrom
Ispalindrom = True

# mengecek string apakah palindrom
for i in range(l):
    # jika terdapat char ke-i tidak sama dengan char ke-(l-1) pada string, maka bukan palindrom
    if string[i] != string[(l-1)-i]:
        Ispalindrom = False

# mencetak kesimpulan string palindrom
if Ispalindrom == True:
    print(f'{string} adalah palindrom')
else:
    print(f'{string} bukan palindrom')