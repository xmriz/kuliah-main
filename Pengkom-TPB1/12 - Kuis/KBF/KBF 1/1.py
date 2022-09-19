# NIM/NAMA    : 16521369_Ahmad Rizki
# Tanggal     : 22 Oktober 2021
# Deskripsi   : Menuliskan  ke layar fungsi f(x), dimana f(x)=sigma(axi+b) 

# KAMUS
# a, b : float
# n : int

# ALGORITMA

# input nilai a, b, dan n
a = float(input('Masukkan nilai a: '))
b = float(input('Masukkan nilai b: '))
n = int(input('Masukkan n: '))

# dimana nilai f(x) dapat disederhanakan menjadi,
hasil = (n*a) + (((n+1)*n*b)/2)

# mencetak hasil
print('Maka nilai dari f(x) adalah', end=' ')
print(hasil)
