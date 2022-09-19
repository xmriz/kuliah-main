N = int(input('Masukkan N: '))

array = [0 for i in range(N)]

for i in range(N):
    array[i] = int(input(f'Masukkan elemen ke {i+1}: '))

p = int(input('Masukkan P: '))

array_geser = [0 for i in range(N)]

for i in range(N):
    array_geser[i-p-1] = array[i]

print(f'Array setelah digeser adalah {array_geser}')