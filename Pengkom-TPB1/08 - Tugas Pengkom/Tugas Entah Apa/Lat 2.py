n = int(input('Berapa jumlah siswa? '))
lulus = 0
tidak_lulus = 0

for i in range(1, n+1):
    nilai = input(f'masukkan predikat mahasiswa ke-{i} : ')
    if nilai is 'A':
        lulus += 1
    elif nilai is 'B':
        lulus += 1
    elif nilai is 'C':
        lulus += 1
    elif nilai is 'D':
        lulus += 1
    else:
        tidak_lulus += 1

print('Lulus =', lulus)
print('Tidak lulus =', tidak_lulus)