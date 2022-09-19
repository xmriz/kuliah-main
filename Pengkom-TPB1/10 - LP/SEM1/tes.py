N = int(input('Masukkan nilai N: '))

matriks = [[0 for j in range(N)] for i in range(N)]
matriks2 = [[0 for j in range(N)] for i in range(N)]

for i in range(N):
    for j in range(N):
        matriks[i][j] = int(input(f'Masukkan elemen pada baris ke-{i+1} kolom ke-{j+1}: '))
        
for i in range(N):
    for j in range(N):
        matriks2[i][j] = matriks[i][j]

isDiagonal = True

for i in range(N):
    matriks2[i][i] = 0
    matriks2[N-1-i][i] = 0

for i in range(N):
    for j in range(N):
        if matriks2[i][j] != 0:
            isDiagonal = False

if isDiagonal == False:
    print('sembarang')
elif isDiagonal == True:
    isSkalar = True
    sample1 = matriks[0][0]
    sample2 = matriks[N-1][0]
    for i in range(N):
        if matriks[i][i] != sample1:
            isSkalar = False
        else:
            for i in range(N):
                if matriks[N-1-i][i] != sample2:
                    isSkalar = False
                else:
                    isSkalar = True
    if isSkalar == True:
        print('skalar')
    else:
        print('diagonal')