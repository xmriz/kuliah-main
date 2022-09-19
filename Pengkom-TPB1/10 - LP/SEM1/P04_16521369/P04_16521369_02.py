# NIM/NAMA  : 16521369/Ahmad Rizki
# Tanggal   : 17 November 2021
# Deskripsi : Program untuk mencetak kode rahasia

# KAMUS
# 

# ALGORITMA
banyak_kata = int(input('Masukkan banyak kata: '))

# membuat array alfabet
def proses(z):
    panjang_kata = int(input(f'Masukkan panjang kata ke-{z+1}: '))
    array_alpa = ['*' for i in range(26)]
    alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(26):
        array_alpa[i] = alfabet[i]

    # membuat tabel frekuensi huruf
    frek = [0 for i in range(26)]

    # input kata
    kata = input(f'Masukkan kata ke-{z+1}: ')

    for char in kata:
        for i in range(26):
            if char == alfabet[i]:
                frek[i] += 1

    print(f'Singkatan kata ke-{z+1}: ', end='')

    for i in range(26):
        if frek[i] != 0:
            print(alfabet[i] + str(frek[i]), end='')
    print()

for z in range(banyak_kata):
    proses(z)