N = int(input('Masukkan banyak soal: '))
key = input('Kunci jawaban: ')
Nhasil = int(input('Masukkan banyaknya hasil ujian: '))

hasil = [0 for i in range(Nhasil)]

for i in range(Nhasil):
    hasil[i] = input(f'Hasil ujian ke {i+1}:')

nilai_tertinggi = 0
banyak_orang_nilai_tinggi = 0

for i in range(Nhasil):
    nilai = 0
    for j in range(N):
        if hasil[i][j] == 'X':
            nilai += 0
        elif hasil[i][j] == key[j]:
            nilai += 3
        elif hasil[i][j] != key[j]:
            nilai -= 1
    if nilai > nilai_tertinggi:
        nilai_tertinggi = nilai
        banyak_orang_nilai_tinggi += 1
    if nilai == banyak_orang_nilai_tinggi:
        banyak_orang_nilai_tinggi += 1

print(f'Terdapat {banyak_orang_nilai_tinggi} dengan nilai tertinggi {nilai_tertinggi}')
