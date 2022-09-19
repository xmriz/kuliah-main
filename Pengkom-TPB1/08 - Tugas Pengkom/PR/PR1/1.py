# SOAl 1

# KAMUS
# a, b : float

# ALGORITMA

# membuat fungsi sisi miring
def sisiMiring(a, b):
    
    # KAMUS LOKAL
    # c = float

    # ALGORITMA
    c = ((a**2) + (b**2))**0.5
    return c


# menginput alas dan tinggi dari segitiga
a = float(input('a: '))
b = float(input('b: '))

# memanggil fungsi sisi miring
hasil = sisiMiring(a, b)

# mencetak hasil
print(hasil)
