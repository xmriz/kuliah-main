def ubahsekali(X):
    # mengubah huruf menjadi huruf setelahnya dalam urutan alfabet
    huruf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(len(huruf)):
        if X == 'z':
            X = 'a' 
        elif X == huruf[i]:
            X = huruf[i+1]
            break
    return X

pesan = input('Masukkan pesan awal: ')
N = int(input('Masukkan nilai N: '))

list_char_pesan = ['*' for i in range(len(pesan))]
for i in range(len(pesan)):
    list_char_pesan[i] = pesan[i]

for a in range(len(pesan)):
    for b in range(N):
        list_char_pesan[a] = ubahsekali(list_char_pesan[a])

print('Pesan akhir adalah', end=' ')
for i in list_char_pesan:
    print(i, end='')