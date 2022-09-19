# NIM/NAMA  : 16521369/Ahmad Rizki
# Tanggal   : 12 Oktober 2021
# Deskripsi : program mencari deret aritmatika suku ke-n

# KAMUS
# a, b, n : int

# Melakukan input untuk nilai a, b, dan n
a = int(input('Masukkan a: '))
b = int(input('Masukkan b: '))
n = int(input('Masukkan n: '))

# Mendefinisikan jumlah awal bilangan
sum = 0

# Melakukan pengulangan dari 1 sampai ke n, kemudian dijumlahkan kedalam variabel sum
for i in range(1,n+1):
    x = a + (i-1)*b
    sum += x

# Menampilkan output dari
print(f'S({n}) = {sum}')