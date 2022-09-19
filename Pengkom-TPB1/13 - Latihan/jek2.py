Na = int(input('Masukkan bilangan N: '))

a = [0 for i in range(Na)]

for i in range(Na):
    a[i] = int(input(f'Masukkan bilangan ke {i+1}: '))

N = Na 

for i in range(Na-1):
    b = [0 for i in range(N-1)]
    for i in range(N-1):
        b[i] = a[i] + a[i+1]
    N -= 1
    a = b

print(f'Bilangan di puncak piramida adalah {b[0]}')