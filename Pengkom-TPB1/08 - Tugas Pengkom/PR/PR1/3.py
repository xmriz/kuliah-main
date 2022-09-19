# SOAl 3

# KAMUS
# x, y : int

# ALGORITMA

# membuat fungsi convert
def convert(code, TC):
    if code == 'F':
        hasil = ((9/5)*TC)+32
    elif code == 'R':
        hasil = (4/5)*TC
    else:
        hasil = TC + 273
    return f'{hasil} {code}'

# mengingput code dan besar suhu dalam celcius
code = input('kode konversi = ')
TC = float(input('Suhu (dalam celcius): '))

# panggil fungsi dan cetak
print(convert(code, TC))