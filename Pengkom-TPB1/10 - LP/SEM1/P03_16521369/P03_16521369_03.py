# NIM/NAMA  : 16521369/Ahmad Rizki
# Tanggal   : 3 November 2021
# Deskripsi : Pr

# KAMUS
# 

# ALGORITMA

# input nyawa ric
nyawa_ric = int(input('Masukkan nyawa awal Ric: '))
nyawa_ric_awal = nyawa_ric
Nr = int(input('Banyak aksi Ric: '))
nyawa_kil = int(input('Masukkan nyawa awal Kil: '))
nyawa_kil_awal = nyawa_kil
Nk = int(input('Banyak aksi Kil: '))


# deklarasi array aksi dengan panjang Nr
r = [0 for i in range(Nr)]
k = [0 for i in range(Nk)]

for i in range()
# mengisi array r dengan aksi2
for i in range(Nr):
    aksiR = input(f'Masukkan aksi Ric ke-{i+1}: ')
    if aksiR == 'H':
        nyawa_ric += round(0.1*(nyawa_ric_awal-nyawa_ric))  
    else: # asumsi tidak ada masukkan aksi berupa string lain selain H
        nyawa_kil -= int(aksiR)

# mengisi array r dengan aksi2
for i in range(Nk):
    aksiK = input(f'Masukkan aksi Kil ke-{i+1}: ')
    if aksiK == 'H':
        nyawa_kil += round(0.1*(nyawa_kil_awal-nyawa_kil))  
    else: # asumsi tidak ada masukkan aksi berupa string lain selain H
        nyawa_ric -= int(aksiK)

if nyawa_ric <= 0:
    print('Pemenang Game adalah Kil')
if nyawa_kil <= 0:
    print('Pemenang Game adalah Ric')