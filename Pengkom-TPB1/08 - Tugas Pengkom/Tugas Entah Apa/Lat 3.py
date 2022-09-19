genap = 0
ganjil = 0
n = int(input('Berapa banyak bilangan? '))

for i in range(1, n+1):
    x = int(input(f'Masukkan bilangan ke-{i} : '))
    if x >= 0:
        if x % 2 == 0:
            genap += 1
        else:
            ganjil += 1
    else:
        break
    
print('Genap :', genap)
print('Ganjil :', ganjil)
