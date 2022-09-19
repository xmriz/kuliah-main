import functions;

def ngitung_panjang_matriks(matriks):
    count = 0
    for i in matriks:
        count += 1
    return count

def cariID(data,ID):
    # Mencari index dimana ID adaa pada data
    # input ->  data : any of data_user or data_game or data_kepemilikan or data_riwayat
    #           ID : string
    # output -> integer

    # I.S. data dan ID terdefinisi
    # F.S. dikembalikan index dimana ID berada pada data 
    
    # KAMUS LOKAL
    # i : integer
    
    # ALGORITMA
    for i in range(ngitung_panjang_matriks(data)):
        if data[i][0] == ID:
            return i

def validasiYN(string):
    # Memvalidasi input dari user, harus 'Y' atau 'N'
    # input -> string : string
    # output -> boolean
    
    # I.S. string terdefinisi
    # F.S. mengembalikan True jika string adalah 'Y' atau 'N' dan False jika sebaliknya
    
    # KAMUS LOKAL
    
    # ALGORITMA
    if (string == 'Y') or (string == 'N'):
        return True
    else:
        print("Jawaban harus 'Y' atau 'N' ")
        print()
        return False

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

def adagame(user_id_login, kepemilikan) :
# proses untuk mengecek terdapat game yang dibeli atau tidak
# I.S user id yang login
# F.S Boolean True/False
    # inisiasi
    idx = 0
    found = False
    # pengecekan user id di data kepemilikan
    while (idx < ngitung_panjang_matriks(kepemilikan)) and (found == False) :
        if (kepemilikan[idx][1] == (user_id_login)) :
            found = True
        else : 
            idx += 1
    # jika valid, akan mereturn True 
    if found == True : 
        return True
    else : 
        return False
    
def arraykosong(array) :
# prosedur arraykosong berfungsi untuk menghitung jumlah elemen yang bukan kosong("")
    count = 0
    for i in range (ngitung_panjang_matriks(array)) :
        if array[i] != "" : 
            count += 1
    return count

def arraybaru(array) :
# prosedur arraybaru berfungsi untuk menghapus element kosong("") di dalam array
    arraybaru = ["" for i in range (arraykosong(array))]
    
    i = 0
    while i  < (ngitung_panjang_matriks(arraybaru)) : 
        for j in range (ngitung_panjang_matriks(array)) :
            if array[j] != "" :
                arraybaru[i] = array[j]
                i += 1
    return arraybaru

# F09
def list_game(folder, user_id) :
# melihat game yang dimiliki oleh user
    # cek apakah user memiliki game atau tidak
    valid1 = adagame(user_id, kepemilikan)
    
    if valid1 == True : # memiliki game
        print("Daftar Game : ")
        
        # Deklarasi Array Kosong yang akan diisi oleh game yang dimiliki
        game_user = ["" for i in range (ngitung_panjang_matriks(kepemilikan))]
        for a in range (ngitung_panjang_matriks(kepemilikan)) : 
            if kepemilikan[a][1] == (user_id) : # user cocok dengan data kepemilikan
                game_user[a] = kepemilikan[a][0] # game yang dimiliki oleh user dimasukkan kedalam array 
        
        # bersihkan element dengan nilai (""
        game_user_b = arraybaru(game_user)
        
        # mencocokan game id yang ada di dalam array game_user_b dengan data di game.csv dan dikeluarkan ouputnya
        i = 0
        while (i < ngitung_panjang_matriks(game_user_b)) :
            for j in range(ngitung_panjang_matriks(game)) :
                if game_user_b[i] == game[j][0] :
                    print(str(i+1)+".", game[j][0], " | ", game[j][1], ' | ' , game[j][4], ' | ' , game[j][2], ' | ', game[j][3])
                    i += 1 
                    if i == ngitung_panjang_matriks(game_user_b) : # jika i == ngitung_panjang_matriks(game_user_b)
                        break
                    else : # jika i < ngitung_panjang_matriks(game_user_b)
                        continue
                    
    elif valid1 == False : # jika tidak memiliki game
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli")