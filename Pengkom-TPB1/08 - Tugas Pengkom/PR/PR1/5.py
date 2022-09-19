# SOAl 5

# KAMUS
# X, a, b : int

# ALGORITMA

# membuat fungsi jumlahKelipatan
def jumlahKelipatan(X, a, b):
    # KAMUS LOKAL
    # sum : int
    sum = 0
    for i in range(a, b+1):
        if i % X == 0:
            sum += 1
    return sum

# menginput X, a, dan b
X = int(input('X : '))
a = int(input('a : '))
b = int(input('b : '))

# panggil fungsi jumlahKelipatan dan cetak
print(f'Keluaran : {jumlahKelipatan(X, a, b)}')
