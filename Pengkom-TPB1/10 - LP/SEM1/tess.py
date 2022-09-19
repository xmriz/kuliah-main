N = int(input('Masukkan nilai N: '))

matriks = [[0 for j in range(N)] for i in range(N)]

for i in range(N):
    for j in range(N):
        matriks[i][j] = int(input(f'Masukkan elemen pada baris ke-{i+1} kolom ke-{j+1}: '))

