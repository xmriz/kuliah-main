n_soal = int(input('Masukkan banyak soal: '))
key = input('Kunci jawaban: ')
n = int(input('Masukkan banyak hasil ujian: '))
jwb = ['*' for i in range(n)]

for i in range(n):
    jwb[i] = input('Hasil ujian ke-{i+1}: ')

for i in range(n):
    benar = 0
    for j in range(n_soal):
        if jwb[i][j] == key[j]:
            benar += 1
    