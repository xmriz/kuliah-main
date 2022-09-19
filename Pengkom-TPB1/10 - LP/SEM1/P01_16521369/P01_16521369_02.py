# NIM/NAMA  : 16521369/Ahmad Rizki
# Tanggal   : 6 Oktober 2020
# Deskripsi : Program untuk membantu Tuan Ric membagi mahasiswa ke dalam sejumlah kelas

# KAMUS
# mahasiswa : int
# kelas : int
# mahasiswa_pas : int
# mahasiswa_lebih : int
# sisa : int
# kelas_pas : int
# kelas_lebih : int

# Melakukan input dari jumlah mahasiswa dan jumlah kelas
mahasiswa = int(input('Masukkan jumlah mahasiswa: '))
kelas = int(input('Masukkan jumlah kelas: '))

# Mendefinisiskan jenis mahasiswa dalam kelas
mahasiswa_pas = mahasiswa//kelas 
mahasiswa_lebih = mahasiswa_pas + 1

# Mendefinisikan jumlah kelas
sisa = mahasiswa % kelas
kelas_pas = kelas - sisa
kelas_lebih = sisa

# melakukan percabangan untuk jumlah mahasiswa setiap kelas sama dan jumlah mahasiswa setiap kelas berbeda
if sisa == 0:
    print(f'Setiap kelas memiliki {mahasiswa_pas} mahasiswa')
else:
    print(f'Ada {kelas_lebih} kelas yang memiliki {mahasiswa_lebih} mahasiswa dan {kelas_pas} yang memiliki {mahasiswa_pas} mahasiswa')
