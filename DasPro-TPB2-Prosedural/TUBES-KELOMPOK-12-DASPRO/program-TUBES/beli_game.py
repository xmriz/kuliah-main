import datetime; import functions

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

def len_manual(string) :
    count = 0
    for i in string :
        count += 1
    return count

def ngitung_panjang_matriks(matriks):
    count = 0
    for i in matriks:
        count += 1
    return count

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

def beli_game():
    # Meminta game yang tersedia pada database
    # I.S. matriks data game, kepemilikan, dan riwayat terdefinisi
    # F.S. data game, kepemilikan, dan riwayat telah diubah

    # KAMUS LOKAL
    # ID, date_string, id_history : string
    # kondisinya, ketemu, syrt : boolean
    # indeks, amount_asked : integer

    # ALGORITMA    
    # Validasi ID ada
    kondisinya = True
    while kondisinya:
        try:
            ID = input("Masukkan ID Game: ")
            ketemu = False

            for j in range(1, ngitung_panjang_matriks(game)):
                if game[j][0] == ID:
                    ketemu = True
                    kondisinya = False
                    indeks = j
                    break
            if ketemu == False:
                print("ID game tidak tersedia, mohon inputkan ID yang benar")
        except ValueError:
            print()

    # Validasi tanggal
    kondisi = True
    while(kondisi):
        format = "%Y"
        date_string = input("Tahun beli: ")
        
        cond = False
        if len_manual(date_string) == 4:
            cond = True

        if cond == False:
            while(True):
                print("Masukan tahun dengan benar, yakni 4 digit tahun dan format YYYY")
                date_string = input("Tahun beli: ")
                if len_manual(date_string) == 4:
                    cond = True
                    break        
        try:
            datetime.datetime.strptime(date_string, format)
            break
        except ValueError:
            print("Tahun yang anda masukan salah. Silahkan masukan kembali tahun beli dengan format YYYY")

    # Mengubah data terbaru
    namagame = game[indeks][1]
    harga = game[indeks][3]
    tahunbeli = date_string
    riwayat += [ID, namagame, harga, userID, tahunbeli]

    game[indeks][5] = game[indeks][5] - 1

    pernah = False
    for al in range(ngitung_panjang_matriks(kepemilikan)):
        if ID == kepemilikan[al][0] and userID == kepemilikan[al][1]:
            pernah = True
            break

    if pernah:
        print("Anda sudah memiliki game tersebut!")
    else: # belum pernah
        kepemilikan += ([ID, userID])

    # Menampilkan ke user bahwa item berhasil diminta
    print()
    print(f"Item {game[indeks][1]} berhasil dibeli!")
    
