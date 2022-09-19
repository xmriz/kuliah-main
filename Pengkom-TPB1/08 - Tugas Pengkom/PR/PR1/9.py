# SOAL 9

# KAMUS
# M1, M2 : matriks of int
# isSame : bool

# deklarasi kedua matriks, dengan asumsi kedua matriks telah terisi
M1 = [[0 for i in range(Nkol1)] for i in range(Nbrs1)]
M2 = [[0 for i in range(Nkol2)] for i in range(Nbrs2)]

# deklarasi isSame awal adalah True
isSame = True

# melakukan percabangan untuk menetukan kesamaan jumlah baris dan kolom
if (Nkol1 == Nkol2) and (Nbrs1 == Nbrs2): 
    for i in range(Nbrs1):
        for j in range(Nkol1):
            if M1[i][j] != M2[i][j]:
                isSame = False
else:
    isSame = False

# mencetak hasil sesuai kondisi isSame
if isSame == True:
    print('Kedua matriks sama')
else:
    print('Kedua matriks tidak sama')
