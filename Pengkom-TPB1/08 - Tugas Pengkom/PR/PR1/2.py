# SOAl 2

# KAMUS
# x, y : int

# ALGORITMA

# membuat fungsi kuadran
def kuadran(x, y):
    if (x > 0) and (y > 0):
        hasil = ('kuadran = 1')
    elif (x < 0) and (y > 0):
        hasil = ('kuadran = 2')
    elif (x < 0) and (y < 0):
        hasil = ('kuadran = 3')
    elif (x > 0) and (y < 0):
        hasil = ('kuadran = 4')
    else:
        hasil = ('Kuadran tidak bisa dihitung')
    return hasil

# menginput nilai x dan y, dengan asumsi keduanya bertipe integer
x = int(input('x = '))
y = int(input('y = '))

# memanggil fungsi kuadran dan mencetaknya
print(kuadran(x, y))