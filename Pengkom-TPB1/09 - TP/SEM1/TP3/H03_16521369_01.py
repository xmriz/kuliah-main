# NIM/NAMA    : 16521369_Ahmad Rizki
# Tanggal     : 16 Oktober 2021
# Deskripsi   : Program yang menerima N buah bilangan dan menuliskan kembali bilangan tersebut, namun terbalik.

# KAMUS
# N : int
# array_awal, array_akhit : array of int

# ALGORITMA

# menginput nilai N
N = int(input('Masukkan N: '))

# deklarasi array dengan panjang N
array_awal = [0 for i in range(N)]
array_akhir = [0 for i in range(N)]

# mengisi array
for i in range(N):
    array_awal[i] = int(input(''))

# membalik urutan dari array
for i in range(N):
    array_akhir[i] = array_awal[(N-1)-i]

# mencetak array satu per satu
print('Hasil dibalik: ')
for i in range(N):
    print(array_akhir[i])
