nbrs = int(input('Masukkan jumlah baris matriks: '))
nkol = int(input('Masukkan jumlah kolom matriks: '))

mat1 = [['*' for j in range(nkol)] for i in range(nbrs)]

for i in range(nbrs):
    for j in range(nkol):
        mat1[i][j] = input(f'Masukkan elemen baris {i+1} kolom {j+1}: ')
    
mat2 = [[0 for j in range(nkol)] for i in range(nbrs)]

for i in range(nbrs):
    for j in range(nkol):
        if mat1[i][j] == '*':
            mat2[i][j] = 1
        else: 
            mat2[i][j] = 0

print(mat1)
print(mat2)
