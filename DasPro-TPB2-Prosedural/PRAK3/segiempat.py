# NIM/Nama	: 16521369/Ahmad Rizki
# Nama file	: segiempat.py
# Topik		: Review Prosedural dengan Bahasa Python
# Tanggal	: 2 Maret 2022
# Deskripsi	: program yang akan membaca N (sebuah integer) berikut C1 dan C2 (dua buah karakter), dan kemudian menuliskan bentuk sebagai 
#             berikut dengan syarat N>0 dan C1 tidak sama dengan C2. Jika syarat tidak dipenuhi, diberikan pesan kesalahan. 


# KAMUS
# N : int
# C1, C2 : char

# ALGORITMA

# input
N = int(input())
C1 = input()[0]
C2 = input()[0]

# percabangan dan perulangan
if (N <= 0) or (C1 == C2):
    print('Masukan tidak valid') 
elif (N <= 2):
    for i in range(N):
        for i in range(N):
            print(C1, end='')
        print()
else:
    print(N*C1)
    for i in range(N-2):
        print(C1, end='')
        for i in range(N-2):
            print(C2, end='')
        print(C1)
    print(N*C1)