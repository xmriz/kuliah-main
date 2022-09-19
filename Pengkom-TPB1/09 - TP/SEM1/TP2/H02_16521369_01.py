# NIM/NAMA    : 16521369_Ahmad Rizki
# Tanggal     : 16 Oktober 2021
# Deskripsi   : Program yang menerima input N dan menuliskan 1 sampai N dalam satu baris

# KAMUS
# N : integer

#ALGORITMA

# Melakukan inisialisasi bilangan N, dengan asumsi N selalu bilangan bulat
N = int(input('Maukkan N: '))

# Melakukan perulangan untuk setiap bilangan bulat dari 1 sampai dengan N
for i in range(1, N+1): 
    print(i, end=' ')   # Mencetak bilangan-bilangan dalam satu baris