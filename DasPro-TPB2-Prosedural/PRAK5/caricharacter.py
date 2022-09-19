N = int(input())

while not (0 < N <= 100):
    print('Masukan salah. Ulangi!')
    N = int(input())

list = []
for i in range(N):
    list += [ord(input())]

CC = input()

if (CC == 'S') or (CC == 's'):
    i = 0
    while not (97 <= list[i] <= 122):
        i += 1
        if i == N:
            break
    if i == N:
        print('Tidak ada huruf kecil')
    else:
        print(1+i, chr(list[i]))

elif (CC == 'L') or (CC == 'l'):
    i = 0
    while not (65 <= list[i] <= 90):
        i += 1
        if i == N:
            break
    if i == N:
        print('Tidak ada huruf besar')
    else:
        print(1+i, chr(list[i]))

elif (CC == 'X') or (CC == 'x'):
    i = 0
    while (65 <= list[i] <= 90) or (97 <= list[i] <= 122):
        i += 1
        if i == N:
            break
    if i == N:
        print('Semua huruf')
    else:
        print(1+i, chr(list[i]))

else:
    print('Tidak diproses')

 


    