def isValid(N):
    if 0<N<=100:
        return True
    else:
        print('Masukan salah. Ulangi!')
        return False

def cond1(array):
    idx = 0
    for i in range(len(array)):
        if array[i] == 0:
            break
        else:
            idx += 1
    if idx == len(array):
        print("Tidak ada 0")
    else:
        print(idx+1)

def cond2(array):
    idx = 0
    for i in range(len(array)):
        if array[i] < 0:
            break
        else:
            idx += 1
    if idx == len(array):
        print("Tidak ada negatif")
    else:
        print(idx+1, array[idx])


def cond3(array):
    idx = 0
    for i in range(len(array)):
        if array[i] > 0:
            break
        else:
            idx += 1
    if idx == len(array):
        print("Tidak ada positif")
    else:
        print(idx+1, array[idx])


next = False
while next == False:
    N = int(input())
    next = isValid(N)

array = [0 for i in range(N)]
for i in range(N):
    array[i] = int(input())

X = int(input())
if X == 0:
    cond1(array)
elif X == -1:
    cond2(array)
elif X == 1:
    cond3(array)
else:
    print('Tidak diproses')




