cap = input('Masukkan kapasitas kendaraan: ')
pel = input('Masukkan jumlah pelanggan (N): ')
jml = input('Masukkan banyak data: ')

if int(cap) < int(pel):
    print('Data tidak benar')
else:
    arr = [0 for i in range(int(jml))]
    itung = [0 for i in range(int(jml))]
    for i in range(int(jml)):
        arr[i] = input('Data ke-' + str(i+1) + ': ')
    for i in arr:
        if i[0] == '+':
            itung[int(i[1])-1] += 1
        else:
            itung[int(i[1])-1] -= 1

