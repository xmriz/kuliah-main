n = int(input('Masukkan banyak elemen: '))

array = [0 for i in range(n)]

for i in range(n):
    array[i] = int(input(f'Masukkan elemen ke-{i+1}: '))

total = array[0]
print(total, end=' ')

for i in range(1, n):
    if array[i] < array[i-1]:
        print(array[i] + array[i-1], end=' ')
    elif array[i] > array[i-1]:
        print(array[i] - array[i-1], end=' ')
    else:
        print(array[i], end=' ')