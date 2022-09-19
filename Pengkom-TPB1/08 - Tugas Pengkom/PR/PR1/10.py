# KAMUS
# M : matriks of int
# isTrue : bool

# Deklarasi isTrue awal
isTrue = True

# deklarasi matriks M dengan asumsi matriks telah terisi
M = [[0 for i in range(Nkol)] for i in range(Nbrs)]

# melakukan percabgan untuk kesamaan jumlah baris dan kolom matriks M
if Nkol == Nbrs:
    # melakukan perulangan untuk mengecek matriks segitiga atas
    for i in range(Nbrs):
        for j in range(Nkol-i):
            if M[i][j] == 0:
                isTrue = False
else:
    isTrue = False

# cetak hasil pengecekan matriks segitiga atas
if isTrue == True:
    print('Matriks segitiga atas')
else:
    print('Bukan matriks segitiga atas')