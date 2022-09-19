lenstr = input('Masukkan panjang string: ')
str = input('Masukkan string: ')

array = ['O','N','L','I','E']
array_itung = [0,0,0,0,0]

""" 
O : 1
N : 2
L : 1
I : 1
E : 1
"""

for i in str:
    if i == 'O':
        array_itung[0] += 1
    elif i == 'N':
        array_itung[1] += 1
    elif i == 'L':
        array_itung[2] += 1
    elif i == 'I':
        array_itung[3] += 1
    elif i == 'E':
        array_itung[4] += 1

print(array_itung)
x = 0
while 0 not in array_itung:
    array_itung[0] -= 1
    array_itung[1] -= 2
    array_itung[2] -= 1
    array_itung[3] -= 1
    array_itung[4] -= 1
    x += 1
    
print(f'Jumlah kata ONLINE yang dapat dibentuk: {x}')   