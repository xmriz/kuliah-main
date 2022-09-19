# NIM/NAMA  : 16521369/Ahmad Rizki
# Tanggal   : 6 Oktober 2020
# Deskripsi : Program yang menentukan Tuan Kil lulus atau tidak lulus pada kelas Tuan Ric dari 4 nilai ujian Tuan Kil

# KAMUS
# nilai1 : float
# nilai2: float
# nilai3 : float
# nilai4 : float
# avg   : float 
# hasil : string

# Melakukan input nilai
nilai1 = float(input('Masukkan nilai ujian 1: '))
nilai2 = float(input('Masukkan nilai ujian 2: '))
nilai3 = float(input('Masukkan nilai ujian 3: '))
nilai4 = float(input('Masukkan nilai ujian 4: '))

#Mendefinisikan rata-rata dari keempat nilai ujian
avg = (nilai1 + nilai2 + nilai3 + nilai4)/4

# Menggunakan percabangan untuk setiap jenis hasil
if nilai1 < 50:
    hasil = 'tidak lulus'
if nilai2 < 50:
    hasil = 'tidak lulus'
if nilai3 < 50:
    hasil = 'tidak lulus'
if nilai4 < 50:
    hasil = 'tidak lulus'
elif avg < 70:
    hasil = "tidak lulus"
else:
    hasil = 'lulus'

# Mencetak hasil
print('Tuan Kil ' + hasil + ' kelas Tuan Ric')