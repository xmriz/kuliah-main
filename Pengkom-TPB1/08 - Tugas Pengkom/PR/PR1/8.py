# SOAL 8

# Bagian A

# deklarasi array of int dengan banyak elemen 100
T1 = [0 for i in range(100)]
T2 = [0 for i in range(100)]

# fungsi untuk mengisi array
def BacaArray():
    for i in range(100):
        T1[i] = int(input(f'array T1 ke-{i}: '))
    for i in range(100):
        T2[i] = int(input(f'array T1 ke-{i}: '))

# memanggil prosedur BacaArray
BacaArray() 

# Bagian B

# deklarasi nilai jumlahSama adalah 0
jumlahSama = 0

for i in range(100):
    if T1[i] == T2[i]:
        jumlahSama += 1

# melakukan percabangan jika jumlahSama sama dengan panjang array maka kedua array sama
if jumlahSama == 100:
    print('Array sama')
else:
    print('Array tidak sama')
