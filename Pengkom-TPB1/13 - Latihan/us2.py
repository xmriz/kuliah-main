n = int(input('Masukkan banyak bilangan: '))

array_nilai = [0 for i in range(n)]

for i in range(n):
    array_nilai[i] = int(input(f'Masukkan nilai ke-{i+1}: '))

# f1
f1 = 1
for i in range(1, n+1):
    f1 *= i

# f2
f2 = 1
for i in range(1, n-1):
    f2 *= i

# banyak kombinasi (n populer)
n_populer = int(f1/(f2*2))

# array_populer
array_populer = []

for i in range(n):
    for j in range(i+1, n):
        array_populer.append( array_nilai[i] + array_nilai[j])

jumlah = 0
for i in array_nilai:
    if i in array_populer:
        jumlah += 1

print(f'Terdapat {jumlah} bilangan Populer')
