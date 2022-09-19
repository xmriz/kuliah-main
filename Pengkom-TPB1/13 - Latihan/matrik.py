#    kolom                baris
M = [[0 for j in range(2)] for i in range(3)]

for i in range(3): #baris
    for j in range(2): # kolom
        M[i][j] = int(input(f'Masukkan baris ke-{i+1} kolom ke-{j+1} : '))

for i in range(3):
    for j in range(2):
        print(M[i][j], end=' ')
    print()