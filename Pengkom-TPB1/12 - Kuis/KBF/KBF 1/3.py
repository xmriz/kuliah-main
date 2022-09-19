# NIM/NAMA    : 16521369_Ahmad Rizki
# Tanggal     : 29 Oktober 2021
# Deskripsi   : Program menentukan jarak yang ditempuh dari input jarak awal dan waktu, dengan kontanta a(percepatan) dan v(kecepatan) yang telah ditentukan

# KAMUS
# s_0, t : int

# ALGORITMA

# Menginput nilai s_0(jarak awal) dan t(waktu tempuh), dengan asumsi s_0 dan t selalu lebih besar dari 0
s_0 = float(input('Masukkan s0: '))
t = float(input("Masukkan t: "))

# Mendefinisikan nilai a dan v sesuai ketentuan
a = 0.01
v = 10

# Mendefiniskan s_t(jarak yang ditempuh)
s_t = (0.5 * a * (t**2)) + (v * t) + s_0

# mencetak nilai s_t
print(s_t)