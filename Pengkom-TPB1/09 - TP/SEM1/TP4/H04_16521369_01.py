# NIM/NAMA    : 16521369_Ahmad Rizki
# Tanggal     : 14 Oktober 2021
# Deskripsi   : Program yang menerima input bilangan bulat A dan B, dan mengembalikan nilai f(x), dimana x dari A sampai B 

# KAMUS
# A, B : int

# Definisikan fungsi f
def f(x):
    # Menghitung nilai fungsi

    # KAMUS LOKAL
    # x, hasil : int

    # ALGORITMA
    hasil = x**2 - 2*x +5
    return hasil

# ALGORITMA UTAMA 

# Melakukan input A dan B, A dan B integer
A = int(input('Masukkan A: '))
B = int(input('Masukkan B: '))

for i in range(A, B+1):
    print(f'f({i}) = {f(i)}')