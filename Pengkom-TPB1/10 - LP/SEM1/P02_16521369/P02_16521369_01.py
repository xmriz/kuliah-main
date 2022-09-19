# NIM/NAMA  : 16521369/Ahmad Rizki
# Tanggal   : 27 Oktober 2020
# Deskripsi : Program untuk mengetahui bilangan dari tuan ric, dimana bilangan tersebut adalah bilagan terkecil yang lebih besar dari bilangan tuan dip, dan memiliki jumlah digit yang sama

# KAMUS
# N, M, sumN, sumM : int

# ALGORITMA

# Menginput bilangan tuan Dip 
N = int(input('Masukkan bilangan tuan Dip (N) : '))

# menghitung jumlah digit dari bilangan tuan dip
sumN = 0
for i in str(N) :
    sumN += int(i) 

# Mendefinisikan bilangan tuan ric sebagai (N+1), dan juga beserta jumlah digitnya
M = N + 1
sumM = 0

# melakukan perulangan hingga kondisi jumlah digit tuan ric sama dengan jumlah digit tuan Dip, yang berarti kondisi yang diminta terpenuhi
while sumM != sumN:
    sumM = 0
    M += 1
    # menghitung jumlah digit dari bilangan tuan ric
    for i in str(M):
        sumM += int(i)
    
#Mencetak bilangan tuan ric
print('Bilangan Tuan Ric adalah', M)

    


