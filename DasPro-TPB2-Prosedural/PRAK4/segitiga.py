# Nama/NIM : Ahmad Rizki/16521369
# Kelas : K03 Daspro

# Program GambarSegitiga
# Input: N : integer
# Output: Jika N > 0 dan ganjil, gambar segitiga sesuai dengan N
#         Jika tidak, tampilkan pesan kesalahan: 

# KAMUS
# Variabel
#    N : int


def GambarSegitiga(N):
# I.S. N > 0 dan N ganjil
# F.S. Gambar segitiga dengan tinggi sebesar N sesuai spesifikasi soal

    # KAMUS LOKAL
    # i : int

    # ALGORITMA
    for i in range(N, 1, -2):
        print(' '*(i-1) + '*'*(N-i+1))
    print(N*'*')
    for i in range(3, N+1, 2):
        print(' '*(i-1) + '*'*(N-i+1))

def IsValid(N):
# menghasilkan true jika N positif dan ganjil, false jika tidak

    # KAMUS LOKAL

    # ALGORITMA
    if (N > 0) and (N % 2 == 1):
        return True
    else:
        return False

# ALGORITMA PROGRAM UTAMA
N = int(input())
if IsValid(N):  # lengkapi dengan pemanggilan fungsi IsValid
    GambarSegitiga(N)    # lengkapi dengan pemanggilan prosedur GambarSegitiga
else: # N tidak positif atau N tidak ganjil
    print("Masukan tidak valid")