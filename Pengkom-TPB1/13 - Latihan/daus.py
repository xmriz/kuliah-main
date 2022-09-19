Nbrs = int(input('Masukkan jumlah baris matriks: '))
Nkol = int(input('Masukkan jumlah kolom matriks: '))

mat = [['*' for j in range(Nkol)] for i in range(Nbrs)]

for i in range(Nbrs):
    for j in range(Nkol):
        mat[i][j] = input(f'Masukkan elemen baris {i+1} kolom {j+1}: ')

