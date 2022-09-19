a = float(input('a = '))
b = float(input('b = '))
delta = float(input('delta = '))
n = (b-a)/delta
jumlah_luas = 0

def fungsi(x):
    return (x**3 + x + 1)

for i in range(1, int(n+1)):
    luas = (fungsi(a + i*delta) + fungsi(a + (i-1)*delta)) * (delta/2)
    jumlah_luas += luas

print('Luas dibawah kurva adalah', jumlah_luas)