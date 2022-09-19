# NIM/NAMA    : 16521369_Ahmad Rizki
# Tanggal     : 16 Oktober 2021
# Deskripsi   : Program yang menentukan apakah B adalah anagram dari A

# KAMUS
# fA, dB, arrayA, arrayB : array of int
# nA, nB : int

# ALGORITMA

# deklarasi frekuensi elemen pada A dan B, dengan asumsi elemen pada array A dan B dari (0-10)
fA = [0 for i in range (11)]
fB = [0 for i in range (11)]

# menginput banyak elemen dari A
nA = int(input('Masukkan banyaknya elemen A: '))
# mengisi array A
arrayA = [0 for i in range(nA)]
for i in range(nA):
    arrayA[i] = int(input(f'Masukkan elemen A ke-{i+1}: '))

# menginput banyak elemen dari B
nB = int(input('Masukkan banyaknya elemen nB: '))
arrayB = [0 for i in range(nB)]
# mengisi array B
for i in range(nB):
    arrayB[i] = int(input(f'Masukkan elemen B ke-{i+1}: '))

# melakukan percabangan banyak elemen A dan B
if nA == nB:
    # mengisi tabel frekuensi dari elemen-elemen pada array A dan B
    for i in range(nA):
        fA[arrayA[i]] += 1
        fB[arrayB[i]] += 1
    # melakukan percabangan untuk frekuensi elemen pada array A sama dengan B
    if fA == fB:
        print('B adalah anagram dari A') # tercetak jika banyak elemen kedua array sama, dan tabel frekuensi tiap elemen juga sama
    else:
        print('B bukan anagram dari A')
else:
    print('B bukan anagram dari A')