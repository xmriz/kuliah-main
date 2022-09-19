u = int(input('Masukkan ukuran peta: '))

matriks = [['.' for i in range(u)] for j in range(u)]

print('Masukkan isi peta: ')

for i in range(u):
    for j in range(u):
        matriks[i][j] = input()

print('Peta yang dibentuk: ')
for i in range(u):
    for j in range(u):
        print(matriks[i][j], end = '')
    print()
