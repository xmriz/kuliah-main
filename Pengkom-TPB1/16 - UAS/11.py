n = int(input('n : '))

T0 = [0 for i in range(n)]
T1 = [0 for i in range(n)]
sum = 0

if n <= 0:
    print('Tidak ada data yang tersedia')
else:
    for i in range(n):
        T0[i] = float(input(f'T0[{i}] : '))
    
    for i in range(n):
        T1[i] = float(input(f'T1[{i}] : '))

    for i in range(n):
        nilai = (T0[i]-T1[i])**2
        sum += nilai
    
    sigma = (1/n)*sum

    print(sigma)