# NIM/NAMA  : 16521369/Ahmad Rizki
# Tanggal   : 17 November 2021
# Deskripsi : 

# KAMUS
# 

# ALGORITMA

def soalgaje(s,a,b):
    ret = s
    for i in s:
        if i == a: 
            ret += str(b)
        else: 
            ret += str(a)
    return ret

A = input("Masukkan karakter 1: ")
B = input("Masukkan karakter 2: ")
n = int(input("Masukkan nilai n: "))

ans = str(A)

for i in range(1,n+1):
    ans = soalgaje(ans,A,B)

print(f"Pola yang didapat: {ans}")