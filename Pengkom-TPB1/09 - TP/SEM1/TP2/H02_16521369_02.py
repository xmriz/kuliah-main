# NIM/NAMA    : 16521369_Ahmad Rizki
# Tanggal     : 17 Oktober 2021
# Deskripsi   : Program yang menerima input N dan menuliskan bilangan 10**x terkecil yang lebih dari N

# KAMUS
# N :integer
# pangkat : integer
# nilai : integer

#ALGORITMA

# Menginput nlai N, dengan N adalah bilagan bulat lebih dari 0
N = int(input('Masukkan N: '))

# Mendefinisikan nilai awal dari pangkat dan nilai
pangkat = 0
nilai = 0

# Melakukan perulangan untuk setiap N yang masih lebih besar dari nilai, dan berhenti ketika nilai telah lebih besar dari nilai N
while N >= nilai:
    nilai = 10**pangkat     #Mendefinisikan ulang nilai sebagai bilangan 10**x
    pangkat += 1

#Mencetak nilai
print(nilai)

