import os
import functions

hasLogin = False
isAdmin = False
userID = ""

user_csv = open("user.csv", 'r')
file_user = user_csv.read()
user = functions.csv_pars(file_user)

game_csv = open("game.csv", 'r')
file_game = game_csv.read()
game = functions.csv_pars(file_game)

riwayat_csv = open("riwayat.csv", 'r')
file_riwayat = riwayat_csv.read()
riwayat = functions.csv_pars(file_riwayat)

kepemilikan_csv = open("kepemilikan.csv", 'r')
file_kepemilikan = kepemilikan_csv.read()
kepemilikan = functions.csv_pars(file_kepemilikan)

# F02 - Register --------------------------------------------------------------------
def validasi_username(user) :
# I.S. String user terdefinisi (berupa string);
# F.S. Apabila string user sesuai dengan kriteria username yang diberikan, maka prosedur akan mengembalikan nilai True.

    # Asumsi string user tidak valid.
    valid = False

    # String user dipecah ke dalam array of user.
    arr_of_user = functions.split_string(user.lower())

    # Mengecek elemen pada array of user.
    for i in arr_of_user :
        # Jika elemen sesuai dengan kriteria pada username, maka elemen tersebut membuat string user memenuhi kriteria username.
        if i == "a" or i == "b" or i == "c" or i == "d" or i == "e" or i == "f" or i == "g" or i == "h" or i == "i" or i == "j" or i == "k" or i == "l" or i == "m" or i == "n" or i == "o" or i == "p" or i == "q" or i == "r" or i == "s" or i == "t" or i == "u" or i == "v" or i == "w" or i == "y" or i == "z" or i == "0 "or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "-" or i == "_" :
            valid = True
        # Jika elemen mengandung unsur/karakter di luar kriteria, maka elemen tersebut membuat username tidak memenuhi spesifikasi.
        else :
            valid = False
            break

    return valid

def register() :
# I.S. Matriks user terdefinisi;
# F.S. Matriks user ditambahkan data user baru.

    # KAMUS LOKAL
    # Deklarasi variabel
    # nama, username, password : string
    # available : boolean
    # i, jumlah_user : int

    # Deklarasi variabel global
    global user

    # ALGORITMA
    # Menerima input nama, username, password dari pengguna baru.
    nama = input("Masukkan nama : ")
    username = input("Masukkan username : ")
    password = input("Masukkan password : ")
    print("")

    # Memeriksa validasi dari input username, apakah memenuhi kriteria atau tidak.
    valid = validasi_username(username)

    # Jika username valid, maka prosedur akan memeriksa apakah username yang diinput tersedia atau tidak.
    if valid :
        # Asumsi username tersedia dan belum pernah dipakai.
        available = True

        # Mengecek username yang ada pada data user. Jika username pengguna baru ditemukan pada username yang ada pada data user, maka username tersebut sudah pernah dipakai dan tidak bisa digunakan lagi.
        for i in range(0, functions.ngitung_panjang_matriks(user)) :
            if user[i][1] == username :
                available = False

                print("Username " + username + " sudah terpakai, silakan menggunakan username lain.")

        # Jika username tersedia, maka prosedur akan menghitung jumlah data user pada matriks user.
        if available :
            jumlah_user = 0
            for i in range(1, functions.ngitung_panjang_matriks(user)) :
                jumlah_user += 1

            # ID user baru merupakan bilangan bulat setelah ID user terakhir pada matriks user.
            new_user_id = str(jumlah_user + 1)

            # Data user baru ditambahkan pada matriks user.
            user += [[new_user_id, username, nama, password, "User", "0"]]

            print("Username " + username + " telah berhasil register ke dalam 'Binomo'.")
    # Jika username tidak valid, maka prosedur akan mencetak pesan kesalahan ke layar.
    else :
        print("Username tidak valid! Username hanya dapat mengandung alfabet A-Z, a-z, underscore “_”, strip “-”, dan angka 0-9.")
# -----------------------------------------------------------------------------------

# F03 - Login -----------------------------------------------------------------------
def login() :
# I.S. Matriks user terdefinisi. Variabel global hasLogin, isAdmin, userID terdefinisi;
# F.S. Mengubah variabel userID dengan id user yang ada pada data, mengubah variabel hasLogin jika pengguna memasukkan username dan password yang benar, dan mengubah variabel isAdmin jika pengguna yang berhasil login memiliki role Admin.

    # KAMUS LOKAL
    # Deklarasi variabel
    # notLogin : boolean
    # username, password : string
    # i : integer

    # Deklarasi variabel global
    global hasLogin
    global isAdmin
    global userID

    # ALGORITMA
    # Ketika pengguna belum login, maka prosedur akan meminta input username dan password untuk masuk ke dalam BNMO.
    hasLogin = False
    username = input("Masukkan username : ")
    password = input("Masukkan password : ")
    print("")

    # Mengecek apakah username dan password sudah terdaftar pada matriks user dan menyocokkan apakah username dan password sudah sesuai.
    for i in range(1, functions.ngitung_panjang_matriks(user)) :
        if (username == user[i][1]) and (password == user[i][3]) :
            # Jika sudah sesuai, maka pengguna berhasil login ke dalam BNMO.
            hasLogin = True
            userID = user[i][0]
            print("Halo " + user[i][2] + "! Selamat datang di 'Binomo'.")

            # Jika pengguna memiliki role Admin, maka isAdmin bernilai True dan pengguna memiliki akses untuk menjalankan perintah khusus role Admin.
            if user[i][4] == "Admin" :
                isAdmin = True

    # Jika setelah melakukan pengecekan tidak ditemukan username atau username dan password tidak cocok, maka prosedur akan mengeluarkan pesan kesalahan.
    if not hasLogin :
        print("Password atau username salah atau tidak ditemukan.")
# -----------------------------------------------------------------------------------

# F16 - Save ------------------------------------------------------------------------
def convert_matrix_to_string(datas) :
# I.S. Matriks user terdefinisi;
# F.S. Matriks user diubah ke bentuk strings sesuai dengan format data csv.

    # KAMUS LOKAL
    # data_string : string
    # data, i : integer

    # ALGORITMA
    # Deklarasi variabel data_string, dimana data_string masih berupa string kosong.
    data_string = ""

    # Melakukan looping pada array yang terdapat pada matriks.
    for data in datas :
        # Melakukan looping pada elemen yang terdapat pada array.
        for i in data :
            # Menyatukan elemen-elemen pada array menjadi satu baris dengan ";" sebagai pemisah (sesuai dengan format csv).
            data_string += str(i) + ";"
        # Pada baris tersebut, masih terdapat pemisah di akhir strings. Prosedur akan menghapus 1 string terakhir yaitu ";".
        data_string = functions.slicing(data_string)
        # Jika sudah terhapus, maka prosedur akan pindah ke baris berikutnya dan mengulang langkah-langkah di atas untuk array berikutnya.
        data_string += "\n"

    return data_string

def save_data(data, filename) :
# I.S. Data dan nama file data terdefinisi;
# F.S. Data yang sudah diperbarui akan disimpan ke file data.

    # KAMUS LOKAL
    
    # ALGORITMA
    # Data yang akan disimpan merupakan data dengan format csv yang sudah diubah dari bentuk matriks.
    data = convert_matrix_to_string(data)

    f = open(filename, "w")
    f.write(data)
    f.close()

def save():
# I.S. Matriks user, game, riwayat, dan kepemilikan terdefinisi;
# F.S. Data user, game, riwayat, dan kepemilikan tersimpan dalam bentuk file csv dan disimpan di folder sesuai dengan input user.

    # KAMUS LOKAL
    # folder_name : string
    # is_exist : boolean

    # ALGORITMA
    # Menerima input nama folder penyimpanan.
    folder_name = input("Masukkan nama folder penyimpanan : ")

    # Mengecek apakah nama folder sudah ada atau belum. Jika sudah ada, maka prosedur akan mengganti folder lama dengan folder baru.
    is_exist = os.path.exists(folder_name)
    # Jika belum ada, maka Prosedur akan membuat folder baru dengan nama folder berdasarkan input pengguna.
    if not is_exist:
        os.makedirs(folder_name)

    # Prosedur melakukan perubahan pada folder penyimpanan.
    os.chdir(folder_name)
    print("")
    print("Saving...")

    # Memanggil fungsi save_data untuk melakukan penyimpanan data pada file csv.
    save_data(user, "user.csv")
    save_data(game, "game.csv")
    save_data(riwayat, "riwayat.csv")
    save_data(kepemilikan, "kepemilikan.csv")

    print("Data telah tersimpan pada folder " + folder_name + "!")
    os.chdir("../")         # Prosedur kembali ke folder asal (supaya tidak berada di dalam folder penyimpanan)
# -----------------------------------------------------------------------------------

# F17 - Exit (nanti revisi lagi nyesuaiin sama main program) ------------------------
def exit():
# I.S. Program masih melakukan looping untuk meminta input command;
# F.S. Program berhenti melakukan looping

    # KAMUS LOKAL
    # confirm_save : string

    # ALGORITMA
    # Menerima input untuk mengonfirmasi penyimpanan data.
    confirm_save = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    # Melakukan validasi terhadap input yang diterima, yaitu Y atau N baik dalam huruf besar maupun huruf kecil.
    while confirm_save.upper() != "Y" or confirm_save.upper() != "N":
        # Jika inputnya tidak valid, maka prosedur akan meminta input ulang sampai didapatkan input yang benar.
        confirm_save = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    # Jika pengguna ingin menyimpan perubahan pada BNMO, maka prosedur akan memanggil prosedur save() dan melakukan penyimpanan data.
    if confirm_save.upper() == "Y":
        save()
# -----------------------------------------------------------------------------------