n = int(input('Masukkan n: '))

mat = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        mat[i][j] = int(input(f'Masukkan elemen ke {i+1} {j+1}: '))

isAtas = True
isBawah = True

for a in range(1,n):
    for b in range(a+1, n+1):
        if mat[n-a][n-b] != 0:
            isAtas = False

for a in range(1,n):
    for b in range(a+1, n+1):
        if mat[n-b][n-a] != 0:
            isBawah = False

if isAtas == True and isBawah == True:
    print('Matriks Diagonal')
elif isAtas == True:
    print('Matriks Segitiga atas')
elif isBawah == True:
    print('Matriks segitiga bawah')
else:
    print('Matriks sembarang')