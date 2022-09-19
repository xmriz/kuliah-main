# NIM/NAMA    : 16521369_Ahmad Rizki
# Tanggal     : 5 Oktober 2021
# Deskripsi   : Program kalkulator sederhana yang menerima 2 buah angka dan sebuah karakter operasi, dan menuliskan hasil perhitungannya

# KAMUS
# A, B  : integer
# opr   : string (hanya berisikan +, -, *, /, %)

# Melakukan input kedua integer dan sebuah operator
A = int(input('Masukkan angka pertama: '))
B = int(input('Masukkan angka kedua: '))
opr = input('Masukkan operator: ')

# Membuat percabangan sesuai operator yang diterima, yang berisikan print hasil operasi. Operator harus berisikan input yang ditentukan.
if opr == '+':
    hasil = A + B
    print(A, '+', B, '=', hasil)
elif opr == '-':
    hasil = A - B
    print(A, '-', B, '=', hasil)
elif opr == '*':
    hasil = A * B
    print(A, '*', B, '=', hasil)
elif opr == '/':    # opr / akan didefinisikan sebagai pembagian dengan pembulatan kebawah (floor divison)
    hasil = A // B
    print(A, '/', B, '=', hasil)
elif opr == '%':
    hasil = A % B
    print(A, '%', B, '=', hasil)
else:
    print('Operator tidak dapat didefiniskan dalam program ini')