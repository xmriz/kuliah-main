lenstr = input('Masukkan panjang string: ')
str = input('Masukkan string: ')

array1 = [str[0]]
array2 = [0]
temp = str[0]
idx = 0

for i in str:
    if i == temp:
        array2[idx] += 1
    else:
        temp = i
        idx += 1
        array2.append(1)
        array1.append(i)



for i in range(len(array1)):
    print(f'{array1[i]}{array2[i]}', end = '')


