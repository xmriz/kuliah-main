# SOAl 4

# KAMUS
# a, b,c : int

# ALGORITMA

# membuat fungsi sort
def urut(a, b, c):
    if a>b>c:
        hasil = f'{a} {b} {c}'
    elif a>c>b:
        hasil = f'{a} {c} {b}'
    elif c>a>b:
        hasil = f'{c} {a} {b}'
    elif c>a>b:
        hasil = f'{b} {a} {c}'
    elif b>c>a:
        hasil = f'{b} {c} {a}'
    else:
        hasil = f'{c} {b} {a}'
    return hasil

# menginput a, b, c
a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))

# panggil fungsi urut, dan cetak
print(f'Keluaran : {urut(a, b, c)}')
            