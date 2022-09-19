# SOAl 5

# KAMUS
# X, a, b : int

# ALGORITMA

# asumsi array sudah terisi
array = [0 for i in range(100)]
# deklarasi nilai awal max dan min
max = array[0]
min = array[0]

for i in range(100):
    if max < array[i]:
        max = array[i]
    if min > array[i]:
        min = array[i]

# menginput pilihan, dengan asumsi pilihan (0-2 saja)
pil = int(input('Pilihan (0-2) : '))

# melalukan percabangan pilihan
if pil == 0:
    print(f'Max = {max}')
    print(f'Min = {min}')
elif pil == 1:
    print(f'Max = {max}')
else:
    print(f'Min = {min}')