N = int(input('Masukkan nilai N: '))
print('Masukkan matriks:')

# insialisasi matrik dengan ukuran N x N
M = [['*' for j in range(N)] for i in range(N)]  

# isi matriks
for i in range(N):
    for j in range(N):
        M[i][j] = input(f'Masukkan elemen baris {i+1} kolom {j+1}: ')

hor = True
ver = True

for i in range(N):
    for j in range(N):
        if M[i][j] == 'B': 
            for a in range(N): # horizontal
                if M[i][a] == 'R':
                    hor = False
            for b in range(N): # vertikal
                if M[b][j] == 'R':
                    ver = False

if hor == False or ver == False:
    print('Ratu tidak aman dari serangan benteng')
else:
    print('Ratu aman dari serangan benteng')