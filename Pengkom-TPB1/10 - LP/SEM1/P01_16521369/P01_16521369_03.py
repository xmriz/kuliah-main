# NIM/NAMA  : 16521369/Ahmad Rizki
# Tanggal   : 6 Oktober 2020
# Deskripsi : Program untuk menentukan tarif parkir Tuan Ric sesuai ketentuan yang ada

# KAMUS
# waktu : int
# jumlah_jam : int
# tarif_after_1jam : int

# Melakukan input waktu parkir dalam menit
waktu = int(input('Masukkan waktu parkir: '))

# Mendefinisikan jumlah jam dan tarif setelah satu jam
jumlah_jam = waktu//60
tarif_after_1jam = 8000 + ((jumlah_jam-1) * 3000)

# Melakukan percabangan
if waktu <= 15:
    print('Tarif yang harus dibayar Tuan Ric sebesar 0 rupiah')
elif jumlah_jam < 1:
    print(f'Tarif yang harus dibayar Tuan Ric sebesar 5000 rupiah')
else:
    if tarif_after_1jam > 20000:
        print(f'Tarif yang harus dibayar Tuan Ric sebesar 20000 rupiah')
    else:
        print(f'Tarif yang harus dibayar Tuan Ric sebesar {tarif_after_1jam} rupiah')
