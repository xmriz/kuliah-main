# NIM/Nama	: 16521369/Ahmad Rizki
# Nama file	: ukuranbaju.py
# Topik		: Review Prosedural dengan Bahasa Python
# Tanggal	: 2 Maret 2022
# Deskripsi	: program yang membaca sebuah nilai T, suatu bilangan integer yang menyatakan temperatur air dalam derajat celcius untuk kondisi 
#             tekanan 1 atm.  Program menuliskan apakah kondisi air tersebut tergantung kepada temperaturnya.

# KAMUS
# T : int

# ALGORITMA
# input
T = int(input())

# percabangan
if T < 0:
    print('PADAT')
elif 0 < T < 100:
    print('CAIR')
elif T > 100:
    print('GAS')
elif T == 0:
    print('ANTARA PADAT-CAIR')
else:
    print('ANTARA CAIR-GAS')
    
