# NIM/NAMA  : 16521369/Ahmad Rizki
# Tanggal   : 3 November 2021
# Deskripsi : Program untuk mengganti char diantara huruf TUANDIP terbanyak pada kata Tuan Dip dengan char R

# KAMUS
# N, max, index : int
# kata, string : str
# frek : array of int

# ALGORITMA

N = int(input('Masukkan panjang kata Tuan Dip: '))
kata = input('Masukkan kata Tuan Dip: ')
string = 'TUANDIP'

# membuat array frekuensi dengan panjang 7
# T : index ke-0
# U : index ke-1
# A : index ke-2
# N : index ke-3
# D : index ke-4
# I : index ke-5
# P : index ke-6
frek = [0 for i in range(7)]

for i in kata:
    if i == 'T':
        frek[0] += 1
    elif i == 'U':
        frek[1] += 1
    elif i == 'A':
        frek[2] += 1
    elif i == 'N':
        frek[3] += 1
    elif i == 'D':
        frek[4] += 1
    elif i == 'I':
        frek[5] += 1
    elif i == 'P':
        frek[6] += 1


# mencari nilai max pada frekuensi
max = 0
for i in frek:
    if i > max:
        max = i


# mencari nilai max berada di index berapa pada frekuensi
index = 0
for i in range(7):
    if frek[i] == max:
        index = i
        break

print(kata.replace(string[index], 'R'))
