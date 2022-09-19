# SOAl 5

# KAMUS
# array : array of int
# isPositive : boolean

# ALGORITMA

# asumsi array dengan banyak elemen 100 sudah terisi
array = [0 for i in range(100)]
# deklarasi isPositive awal sebagai True
isPositive = True
# lakukan pengecekan untuk setiap elemen array
for i in array:
    if array[i] < 0:
        isPositive = False
# cetak array
if isPositive == True:
    print('Semua elemen array positif')
else:
    print('Tidak semua elemen array positif')