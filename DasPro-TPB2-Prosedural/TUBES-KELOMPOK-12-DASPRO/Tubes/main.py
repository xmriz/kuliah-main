import os
import datetime
import argparse

# -------------------------------- Fungsi Bawaan ------------------------------------
def ngitung_line_csv(csv) :
# Menghitung jumlah baris pada data

    # KAMUS LOKAL
    # lines : int
    # i : char

    # ALGORITMA
    # Deklarasi variabel lines
    lines = 0
    # Mengecek nilai i pada string csv
    for i in csv :
        # Jika baris sudah berganti, maka jumlah baris bertambah 1
        if i == "\n" :
            lines += 1
    return lines

def ngitung_kolom_csv(csv) :
# Menghitung jumlah kolom pada data

    # KAMUS LOKAL
    # kolom : int
    # i : char

    # ALGORITMA
    # Deklarasi variabel kolom
    kolom = 0
    # Mengecek nilai i pada strings csv
    for i in csv :
        # Jika kolom sudah berganti (pada data csv kolom dipisahkan dengan ";"), maka jumlah kolom bertambah 1
        if i == ";" :
            kolom += 1
        # Jika kolom sudah habis (";" sudah tidak ada lagi dan sudah berganti baris), maka jumlah kolom merupakan jumlah yang sebelumnya ditambah dengan 1
        if i == "\n" :
            return kolom + 1

def len_manual(string) :
# Menghitung jumlah karakter pada string

    # KAMUS LOKAL
    # count : int
    # i : char

    # ALGORITMA
    # Deklarasi variabel count
    count = 0
    # Menghitung jumlah karakter pada string
    for i in string :
        count += 1
    return count

def slicing(string) :
# Menghapus karakter terakhir pada string

    # KAMUS LOKAL
    # sliced : string
    # length, count : int
    # i : char

    # Deklarasi fungsi/prosedur
    # function len_manual (string : string) -> integer
    # Menghitung jumlah karakter/huruf pada string

    # ALGORITMA
    # Deklarasi variabel
    sliced = ""
    count = 0
    length = len_manual(string)
    # Mengecek nilai i pada string
    for i in string :
        # Jika panjang string baru masih kurang dari panjang string awal, maka karakter/huruf dari string lama akan terus ditambah ke string baru
        if count < length - 1 :
            sliced += i
        count += 1
    return sliced

def split_string(string) :
# Memecah setiap karakter/huruf dalam string ke dalam array

    # KAMUS LOKAL
    # string_splitted : array of char
    # i : int

    # ALGORITMA
    # Deklarasi array of character
    string_splitted = ["" for i in string]
    # Untuk setiap karakter dalam string, karakter akan dimasukkan ke dalam array of character
    for i in range(len_manual(string)) :
        string_splitted[i] += string[i]
    return string_splitted

def csv_pars(csv) :
# Mengubah data csv (yang sudah di read) menjadi matriks data

    # KAMUS LOKAL
    # panjang_line, banyak_kolom : int
    # file_parsed : array [1..banyak_kolom] of array [1..panjang_line] of string

    # Deklarasi fungsi/prosedur
    # function ngitung_line_csv (csv : string) -> integer
    # Menghitung jumlah baris pada data
    # function ngitung_kolom_csv (csv : string) -> integer
    # Menghitung jumlah kolom pada data

    # ALGORITMA
    # Menghitung jumlah baris dan kolom pada data csv
    panjang_line = ngitung_line_csv(csv)
    banyak_kolom = ngitung_kolom_csv(csv)

    # Deklarasi matriks data
    file_parsed = [[0 for i in range(banyak_kolom)] for i in range(panjang_line)]
    
    # Pengisian matriks data
    data = 0
    while data < panjang_line :
        counter = 0
        item = ""
        for j in csv :
            if j == "\n" :   
                file_parsed[data][counter] = item
                data += 1
                counter = 0
                item = ""
            elif j == ";":
                file_parsed[data][counter] = item
                counter += 1
                item = ""
            else:
                item += j
    return(file_parsed)

def ngitung_panjang_matriks(matriks) :
# Menghitung banyaknya data dalam bentuk array pada matriks

    # KAMUS LOKAL
    # count : int
    # i : array of string

    # ALGORITMA
    # Deklarasi variabel count
    count = 0
    # Menghitung jumlah data
    for i in matriks :
        count += 1
    return count
# -----------------------------------------------------------------------------------

# F02 - Register --------------------------------------------------------------------
def cari_string(i) :
# Menghasilkan True atau False sesuai dengan kriteria karakter/huruf pada string
    
    # KAMUS LOKAL

    # ALGORITMA
    # Jika i memenuhi salah satu kriteria di bawah ini, maka fungsi akan mengembalikan nilai True
    if i == "a" or i == "b" or i == "c" or i == "d" or i == "e" or i == "f" or i == "g" or i == "h" or i == "i" or i == "j" or i == "k" or i == "l" or i == "m" or i == "n" or i == "o" or i == "p" or i == "q" or i == "r" or i == "s" or i == "t" or i == "u" or i == "v" or i == "w" or i == "x" or i == "y" or i == "z" or i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "-" or i == "_" :
        return True

def validasi_username(user) :
# Mengembalikan nilai True jika string user sesuai dengan kriteria username yang diberikan

    # KAMUS LOKAL
    # valid : boolean
    # arr_of_user : array of character

    # Deklarasi fungsi/prosedur
    # function cari_string (i : string) -> boolean
    # Menghasilkan True atau False sesuai dengan kriteria karakter/huruf pada string
    # function split_string (string : string) -> array of char
    # Memecah setiap karakter/huruf dalam string ke dalam array 

    # ALGORITMA
    # Asumsi string user tidak valid.
    valid = False

    # String user dipecah ke dalam array of user.
    arr_of_user = split_string(user.lower())
    
    # Mengecek elemen pada array of user.
    for i in arr_of_user :
        # Jika elemen ditemukan pada kriteria username, maka elemen tersebut membuat string user memenuhi kriteria username.
        if cari_string(i) :
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
    # valid, available : boolean
    # i, jumlah_user : int
    # new_user_id : string

    # Deklarasi variabel global
    global user

    # Deklarasi fungsi/prosedur
    # function validasi_username (user : string) -> boolean
    # Mengembalikan nilai True jika string user sesuai dengan kriteria username yang diberikan
    # function ngitung_panjang_matriks (matriks : array of array of string) -> integer
    # Menghitung banyaknya data dalam bentuk array pada matriks

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
        for i in range(0, ngitung_panjang_matriks(user)) :
            if user[i][1] == username :
                available = False

                print("Username " + username + " sudah terpakai, silakan menggunakan username lain.")

        # Jika username tersedia, maka prosedur akan menghitung jumlah data user pada matriks user.
        if available :
            jumlah_user = 0
            for i in range(1, ngitung_panjang_matriks(user)) :
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
# I.S. Matriks user terdefinisi. Variabel global notLogin, isAdmin, userID terdefinisi;
# F.S. Mengubah variabel userID dengan id user yang ada pada data, mengubah variabel notLogin jika pengguna memasukkan username dan password yang benar, dan mengubah variabel isAdmin jika pengguna yang berhasil login memiliki role Admin.

    # KAMUS LOKAL
    # Deklarasi variabel
    # notLogin : boolean
    # username, password : string
    # i : integer

    # Deklarasi variabel global
    global notLogin
    global isAdmin
    global userID

    # Deklarasi fungsi/prosedur
    # function ngitung_panjang_matriks (matriks : array of array of string) -> integer
    # Menghitung banyaknya data dalam bentuk array pada matriks

    # ALGORITMA
    # Ketika pengguna belum login, maka prosedur akan meminta input username dan password untuk masuk ke dalam BNMO.
    notLogin = True
    username = input("Masukkan username : ")
    password = input("Masukkan password : ")
    print("")

    # Mengecek apakah username dan password sudah terdaftar pada matriks user dan menyocokkan apakah username dan password sudah sesuai.
    for i in range(1, ngitung_panjang_matriks(user)) :
        if (username == user[i][1]) and (password == user[i][3]) :
            # Jika sudah sesuai, maka pengguna berhasil login ke dalam BNMO.
            notLogin = False
            userID = user[i][0]
            print("#------------------------------------------------#")
            print("Halo " + user[i][2] + "! Selamat datang di 'Binomo'.")

            # Jika pengguna memiliki role Admin, maka isAdmin bernilai True dan pengguna memiliki akses untuk menjalankan perintah khusus role Admin.
            if user[i][4] == "Admin" :
                isAdmin = True

    # Jika setelah melakukan pengecekan tidak ditemukan username atau username dan password tidak cocok, maka prosedur akan mengeluarkan pesan kesalahan.
    if notLogin :
        print("Password atau username salah atau tidak ditemukan.")
# -----------------------------------------------------------------------------------

# F04 - Tambah Game -----------------------------------------------------------------
def tambah_game(mtrxgametemp,isAdmin):
    #Fungsi Menambahkan game baru pada matriks game csv
    #I.S. mtrxgametemp, isAdmin terdefinisi
    #F.S  Game baru berhasil ditambahkan ke mtrxgametemp

    #KAMUS LOKAL
    #jumlahdata: intetger
    #nama_game,kategori_game,gameid,tahun_rilis,harga_game,stok_awal: string
    #mtrxgametemp: array of array of string and integer
    #game_baru: array of string and integer
    #isAdmin,sama: boolean

    #Deklarasi Fungsi/Prosedur
    # function ngitung_panjang_matriks (matriks : array of array of string) -> integer
    # Menghitung banyaknya data dalam bentuk array pada matriks

    #isdigit(strng: string) -> boolean
    #Mengecek apakah sebuah string merupakan angak atau tidak

    #ALGORITMA
    if not isAdmin:
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
    
    else:
        jumlah_data = ngitung_panjang_matriks(mtrxgametemp)
        if jumlah_data < 10: #Memberikan game id pada game baru yang akan ditambahkan
            gameid = "GAME00" + str(jumlah_data)
        elif 10 <= jumlah_data < 100:
            gameid = "GAME0" + str(jumlah_data)
        else:
            gameid = "GAME" + str(jumlah_data)

        sama = False
        nama_game = input("Masukkan nama game: ")
        for i in mtrxgametemp: #Mengecek apakah ada game yang sama di toko
            if nama_game.upper() == i[1].upper():
                sama = True
                
        while sama: #Mengulangi hingga mendapatkan game yang sama di toko
            sama = False
            print("")
            print("Game tersebut sudah terdapat di toko!\nMohon masukkan nama game berbeda!")
            print("")
            nama_game = input("Masukkan nama game: ")
            for i in mtrxgametemp: 
                if nama_game.upper() == i[1].upper():
                    sama = True
                    

        kategori_game = input("Masukkan kategori game: ")

        tahun_rilis = input("Masukkan tahun rilis: ") 
        while tahun_rilis != "" and not tahun_rilis.isdigit(): #Looping sampai mendapatkan input tahun_rilis integer/string kosong
            print("Tolong berikan masukkan yang valid!")
            tahun_rilis = input("Masukkan tahun rilis: ")

        harga_game = input("Masukkan harga: ") 
        while harga_game != "" and not harga_game.isdigit(): #Looping sampai mendapatkan input harga_game integer/string kosong
            print("Tolong berikan masukkan yang valid!")
            harga_game = input("Masukkan harga: ")

        stok_awal = input("Masukkan stok awal: ") 
        while stok_awal != "" and not stok_awal.isdigit(): #Looping sampai mendapatkan input stok_awal integer/string kosong
            print("Tolong berikan masukkan yang valid!")
            stok_awal = input("Masukkan stok awal: ")

        while nama_game == "" or kategori_game == "" or tahun_rilis == "" or harga_game == "" or stok_awal == "": 
            #Mengecek apakah ada input yang kosong atau tidak dan akan diulangi sampai semua input terisi 
            print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
            
            sama = False
            nama_game = input("Masukkan nama game: ")
            for i in mtrxgametemp: #Mengecek apakah ada game yang sama di toko
                if nama_game.upper() == i[1].upper():
                    sama = True
    
            while sama: #Mengulangi hingga mendapatkan game yang sama di toko
                sama = False
                print("")
                print("Game tersebut sudah terdapat di toko!\nMohon masukkan nama game berbeda!")
                nama_game = input("Masukkan nama game: ")
                print("")
                for i in mtrxgametemp:
                    if nama_game.upper() == i[1].upper():
                        sama = True
                        
            
            kategori_game = input("Masukkan kategori game: ")
            
            tahun_rilis = input("Masukkan tahun rilis: ") 
            while tahun_rilis != "" and not tahun_rilis.isdigit(): #Looping sampai mendapatkan input tahun_rilis integer/string kosong
                print("Tolong berikan masukkan yang valid!")
                tahun_rilis = input("Masukkan tahun rilis: ")

            harga_game = input("Masukkan harga: ") 
            while harga_game != "" and not harga_game.isdigit(): #Looping sampai mendapatkan input harga_game integer/string kosong
                print("Tolong berikan masukkan yang valid!")
                harga_game = input("Masukkan harga: ")

            stok_awal = input("Masukkan stok awal: ") 
            while stok_awal != "" and not stok_awal.isdigit(): #Looping sampai mendapatkan input stok_awal integer/string kosong
                print("Tolong berikan masukkan yang valid!")
                stok_awal = input("Masukkan stok awal: ")
            
        else: #Jika semua input sudah terisi akan menambahkan game baru ke dalam matriks game
            print(f"Selamat! Berhasil menambahkan game {nama_game}")
            gamebaru = [gameid,nama_game,kategori_game,int(tahun_rilis),int(harga_game),int(stok_awal)]
            mtrxgametemp += [gamebaru]
            return mtrxgametemp #Mengembalikan matriks game yang terdapat di toko baru yang sudah di update
# -----------------------------------------------------------------------------------

# F05 - Mengubah Game Pada Toko -----------------------------------------------------
def ubah_game(mtrxgametemp,isAdmin):
    #Fungsi akan mengubah data game sesuai dengan id game yang di input
    #I.S. mtrxgametemp, isAdmin terdefinisi
    #F.S. Game berhasil diubah pada mtrxgametemp

    #KAMUS LOKAL
    #mtrxgametemp: array of array of string and integer
    #isAdmin, ada: boolean
    #panjang_matrix, index, i: integer
    #id_yang_diubah,nama_diubah,kategori_diubah,tahun_diubah,harga_diubah: string

    #Deklarasi Fungsi/Prosedur
    # function ngitung_panjang_matriks (matriks : array of array of string) -> integer
    # Menghitung banyaknya data dalam bentuk array pada matriks

    #ALGORITMA
    if not isAdmin: #Jika bukan admin
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
    else: #Jika Admin
        panjang_matrix = ngitung_panjang_matriks(mtrxgametemp)
        id_yang_diubah = input("Masukkan id game yang akan diubah: ").upper()
        ada = False
        index = 0
        for i in range(1,panjang_matrix): #Mengecek apakah ada game yang memiliki id sesuai dengan input9
            if mtrxgametemp[i][0] == id_yang_diubah:
                ada = True
                index = i
        if ada: #Jika ada
            nama_diubah = input("Masukkan nama game: ") 
            if nama_diubah != "": #Jika input bukan string kosong maka nama game akan diubah sesuai input
                mtrxgametemp[index][1] = nama_diubah
            
            kategori_diubah = input("Masukkan kategori game: " )
            if kategori_diubah != "": #Jika input bukan string kosong maka kategori game akan diubah sesuai input
                mtrxgametemp[index][2] = kategori_diubah
            
            tahun_diubah = input("Masukkan tahun rilis: ")
            while tahun_diubah != "" and not tahun_diubah.isdigit(): #Jika input bukan string kosong atau angka maka akan meminta input yang valid lagi
                print("Tolong berikan masukan yang valid!")
                tahun_diubah = input("Masukkan tahun rilis: ")
            if tahun_diubah != "": #Jika input bukan string kosong maka tahun akan diubah sesuai input
                mtrxgametemp[index][3] = int(tahun_diubah)
            
            harga_diubah = input("Masukkan harga: ")
            while harga_diubah != "" and not harga_diubah.isdigit(): #Jika input bukan string kosong atau angka maka akan meminta input yang valid lagi
                print("Tolong berikan masukkan yang valid!")
                harga_diubah = input("Masukkan harga: ") 
            if harga_diubah != "": #Jika input bukan string kosong maka harga akan diubah sesuai input
                mtrxgametemp[index][4] = int(harga_diubah)

            print(f"{id_yang_diubah} berhasil diubah")
            return mtrxgametemp #Mengembalikan mtrxgametmep yang sudah diubah
        
        else:
            print("Tidak ada game yang memiliki id tersebut!")
            return mtrxgametemp #Mengembalikan mtrxgametemp inisial
# -----------------------------------------------------------------------------------

#F06 - Mengubah Stok Game di Toko ---------------------------------------------------
def ubah_stok(mtrxgametemp,isAdmin):
    #Melakukan perubahan stok pada matriks game yang terdapat di toko
    #I.S. mtrxgametemp,isAdmin terdefinisi
    #F.S. Stok game pada toko berhasil diubah
    
    #KAMUS LOKAL
    #id_yang_diubah,operation: string
    #ada,angka_valid: boolean
    #banyak_berubah,index: integer

    #Deklarasi Fungsi/Prosedur
    # function ngitung_panjang_matriks (matriks : array of array of string) -> integer
    # Menghitung banyaknya data dalam bentuk array pada matriks

    #ALGORITMA
    if not isAdmin:
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
    else:
        id_yang_diubah = input("Masukkan ID game: ").upper()
        ada = False
        angka_valid = False
        while not angka_valid: #Melakukan validasi input apakah integer atau tidak dan akan diulangi sampai mendapatkan input integer
            try:
                banyak_berubah = int(input("Masukkan jumlah: "))
            except ValueError:
                print("Tolong berikan masukkan yang valid!")
                continue
            else:
                angka_valid = True
        index = 0
        if banyak_berubah < 0: #Mengecek apakah game ditambah atau dikurang
            operation = "dikurangi"
        else:
            operation = "ditambahkan"
        for i in range(1,ngitung_panjang_matriks(mtrxgametemp)): #Looping untuk mencari apakah ada game dengan id sesuai input di toko
            if mtrxgametemp[i][0] == id_yang_diubah: #Jika game ada akan dilakukan perubahan stok
                ada = True
                sisa_stock = int(mtrxgametemp[i][5]) + banyak_berubah
                index = i
        
        if not ada: #Jika game tidak ada akan di mencetak tidak ada game dengan id tersebut
            print("Tidak ada game dengan ID tersebut!")
            return mtrxgametemp
        else: #Matriks akan diupdate dengan perubahan stok
            if sisa_stock >= 0: #Jika dicoba melakukan perubahan stok, stok game masih lebih besar sama dengan 0, maka matriks akan di update
                mtrxgametemp[index][5] = sisa_stock
                print(f"Stok game {mtrxgametemp[index][1]} berhasil {operation}. Stok Sekarang {sisa_stock}")
            else: #Jika dicoba melakukan perubahan stok, stok game dibawah 0. Maka matriks tidak akan di update.
                print(f"Stok game {mtrxgametemp[index][1]} gagal {operation}. Stok Sekarang {mtrxgametemp[index][5]} (<{-1*banyak_berubah})")
            return mtrxgametemp #Mengembalikan matriks yang semula
# -----------------------------------------------------------------------------------

#F07 - Listing Game Di Toko ---------------------------------------------------------
def list_game_toko(mtrxgametemp):
    #Prosedur akan menerima parameter berupa matrix yang berisi game yang terdapat pada toko dan akan mencetak 

    #I.S. Matriks data game yang terdapat di toko
    #F.S. Matriks data yang terdapat di toko dengan urutan sesuai input

    #KAMUS LOKAL
    #sorted_matrix,mtrxgametemp: array of array of string and integer
    #skema_sortig: string
    #panjang_matrix,i,j: integer
    #valid: boolean

    #Deklarasi Fungsi/Prosedur
    # function ngitung_panjang_matriks (matriks : array of array of string) -> integer
    # Menghitung banyaknya data dalam bentuk array pada matriks
    
    #ALGORITMA
    sorted_matrix = [] 
    for i in mtrxgametemp: #Looping untuk copy mtrxgametemp ke dalam sorted_matrix yang akan dicetak
        sorted_matrix += [i]
    skema_sorting = input("Skema sorting: ").upper()
    panjang_matrix = ngitung_panjang_matriks(sorted_matrix)
    valid = False

    if skema_sorting == "TAHUN-": #Melakukan bubble sort untuk mengurutkan berdasarkan tahun secara descending (menurun)
        valid = True
        for i in range(1,panjang_matrix-1): 
            for j in range(1,panjang_matrix-i):
                if int(sorted_matrix[j][3]) < int(sorted_matrix[j+1][3]):
                    sorted_matrix[j+1],sorted_matrix[j] = sorted_matrix[j],sorted_matrix[j+1]
    
    elif skema_sorting == "TAHUN+": #Melakukan bubble sort untuk mengurutkan berdasarkan tahun secara ascending (meningkat)
        valid = True
        for i in range(1,panjang_matrix-1):
            for j in range(1,panjang_matrix-i):
                if int(sorted_matrix[j][3]) > int(sorted_matrix[j+1][3]):
                    sorted_matrix[j+1],sorted_matrix[j] = sorted_matrix[j],sorted_matrix[j+1]

    elif skema_sorting == "HARGA-": #Melakukan bubble sort untuk mengurutkan berdasarkan harga secara descending (menurun)
        valid = True
        for i in range(1,panjang_matrix-1):
            for j in range(1,panjang_matrix-i):
                if int(sorted_matrix[j][4]) < int(sorted_matrix[j+1][4]):
                    sorted_matrix[j+1],sorted_matrix[j] = sorted_matrix[j],sorted_matrix[j+1]

    elif skema_sorting == "HARGA+": #Melakukan bubble sort untuk mengurutkan berdasarkan harga secara ascending (meningkat)
        valid = True
        for i in range(1,panjang_matrix-1):
            for j in range(1,panjang_matrix-i):
                if int(sorted_matrix[j][4]) > int(sorted_matrix[j+1][4]):
                    sorted_matrix[j+1],sorted_matrix[j] = sorted_matrix[j],sorted_matrix[j+1]

    elif skema_sorting == "": #sorted matrix tetap sesuai dengan game id
        valid = True
                
    else: #Melakukan pengecekan apakah skema sorting valid atau tidak
        valid = False
    
    idterpanjang = 7
    namaterpanjang = 0
    kategoriterpanjang = 0
    tahunterpanjang = 0
    hargaterpanjang = 0
    stokterpanjang = 0
    
    for i in range(panjang_matrix): #Looping untuk menghitung kata terpanjang pada setiap elemen data
        if ngitung_panjang_matriks(str(sorted_matrix[i][1])) > namaterpanjang:
            namaterpanjang = ngitung_panjang_matriks(str(sorted_matrix[i][1])) + 2
        if ngitung_panjang_matriks(str(sorted_matrix[i][2])) > kategoriterpanjang:
            kategoriterpanjang = ngitung_panjang_matriks(str(sorted_matrix[i][2])) + 2
        if ngitung_panjang_matriks(str(sorted_matrix[i][3])) > tahunterpanjang: 
            tahunterpanjang = ngitung_panjang_matriks(str(sorted_matrix[i][3])) + 2
        if ngitung_panjang_matriks(str(sorted_matrix[i][4])) > hargaterpanjang:
            hargaterpanjang = ngitung_panjang_matriks(str(sorted_matrix[i][4])) + 2
        if ngitung_panjang_matriks(str(sorted_matrix[i][5])) > stokterpanjang:
            stokterpanjang = ngitung_panjang_matriks(str(sorted_matrix[i][5])) + 2
            
    if valid: #Jika skema sorting valid akan mencetak list game pada toko sesuai dengan pilihan sorting
        for i in range(panjang_matrix):   
            print(f"  {sorted_matrix[i][0]}  ",end=" "*  (idterpanjang - ngitung_panjang_matriks(str(sorted_matrix[i][0]))))
            print(f"|",end="  ")
            print(f"{sorted_matrix[i][1]}",end=" "* (namaterpanjang - ngitung_panjang_matriks(str(sorted_matrix[i][1]))))
            print("|",end="  ")
            print(f"{sorted_matrix[i][2]}",end=" "* (kategoriterpanjang - ngitung_panjang_matriks(str(sorted_matrix[i][2]))))
            print("|",end="  ")
            print(f"{sorted_matrix[i][3]}",end=" " * (tahunterpanjang - ngitung_panjang_matriks(str(sorted_matrix[i][3]))))
            print("|",end="  ")
            print(f"{sorted_matrix[i][4]}",end=" " * (hargaterpanjang - ngitung_panjang_matriks(str(sorted_matrix[i][4]))))
            print("|",end="  ")
            print(f"{sorted_matrix[i][5]}")


    else: #Jika skema sorting tidak valid akan mencetak skema sorting tidak valid
        print("Skema sorting tidak valid!")
# -----------------------------------------------------------------------------------

#F08 - Membeli Game -----------------------------------------------------------------
def beli_game(mtrxgametemp,riwayattemp,kepemilikantemp):
    # Meminta game yang tersedia pada database
    # I.S. matriks data game, kepemilikan, dan riwayat terdefinisi
    # F.S. data game, kepemilikan, dan riwayat telah diubah

    # KAMUS LOKAL
    # ID, date_string, id_history : string
    # kondisinya, ketemu, syrt : boolean
    # indeks, amount_asked : integer

    #Deklarasi Fungsi/Prosedur
    # function ngitung_panjang_matriks (matriks : array of array of string) -> integer
    # Menghitung banyaknya data dalam bentuk array pada matriks
        
    # function len_manual (string : string) -> integer
    # Menghitung jumlah karakter/huruf pada string


    # ALGORITMA    
    # Validasi ID ada
    kondisinya = True
    while kondisinya:
        try:
            gameid = input("Masukkan ID Game: ").upper()
            ketemu = False

            for j in range(1, ngitung_panjang_matriks(mtrxgametemp)):
                if mtrxgametemp[j][0] == gameid:
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
    namagame = mtrxgametemp[indeks][1]
    harga = mtrxgametemp[indeks][3]
    tahunbeli = date_string

   

    pernah = False
    for al in range(ngitung_panjang_matriks(kepemilikantemp)):
        if gameid == kepemilikantemp[al][0] and userID == kepemilikantemp[al][1]:
            pernah = True
            break

    if pernah:
        print("Anda sudah memiliki game tersebut!")
    else: # belum pernah
        kepemilikantemp += [[gameid, userID]]
        mtrxgametemp[indeks][5] -= 1
        # Menampilkan ke user bahwa item berhasil dibeli
        print()
        print(f"Game {mtrxgametemp[indeks][1]} berhasil dibeli!")
        riwayattemp += [[gameid, namagame, harga, userID, tahunbeli]]
# -----------------------------------------------------------------------------------

#F09 - Melihat Game yang Dimiliki ---------------------------------------------------
def list_game(userID,kepemilikantemp,mtrxgametemp) :
    #Prosedur akan mengeluarkan list game yang dimiliki user
    #I.S. userID,kepemilkantemp,mtrxgametemp terdefinisi
    #F.S. Mengeluarkan list game yang dimiliki oleh user

    #KAMUS LOKAL
    #id_game_yang_dimilikii: array of string
    #data_game_yang_dimiliki: array of string and integer
    #idterpanjang,namaterpanjang,kategoriterpanjang,tahunterpanjang,hargaterpanjang: integer

    #Deklarasi Fungsi/Prosedur
    # function ngitung_panjang_matriks (matriks : array of array of string) -> integer
    # Menghitung banyaknya data dalam bentuk array pada matriks

    #ALGORITMA
    id_game_yang_dimiliki = [] 
    for i in range(ngitung_panjang_matriks(kepemilikantemp)): #Mencari id game yang dari kepemilikantemp
        if kepemilikantemp[i][1] == userID:
            id_game_yang_dimiliki += [kepemilikantemp[i][0]]
    data_game_yang_dimiliki = [] 
    for i in range(ngitung_panjang_matriks(mtrxgametemp)): #Mencari data dari game yang dimiliki
        for j in range(ngitung_panjang_matriks(id_game_yang_dimiliki)):
            if mtrxgametemp[i][0] == id_game_yang_dimiliki[j]:
                data_game_yang_dimiliki += [mtrxgametemp[i]]
        
    idterpanjang = 7
    namaterpanjang = 0
    kategoriterpanjang = 0
    tahunterpanjang = 0
    hargaterpanjang = 0

    print("")
    print("Data game yang dimiliki: ")

    if data_game_yang_dimiliki == []: #Jika tidak memiliki game
        print("Maaf, kamu belum membeli game. Ketik perintah buy_game untuk beli.")
    else: #Jika memiliki game
        data_game_yang_dimiliki = [["ID","NAMA","KATEGORI","TAHUN","HARGA","STOK"]] + data_game_yang_dimiliki 
        for i in range(ngitung_panjang_matriks(data_game_yang_dimiliki)): #Looping untuk menghitung kata terpanjang dari setiap data elemen data_game_yang_dimiliki
            if ngitung_panjang_matriks(str(data_game_yang_dimiliki[i][1])) > namaterpanjang:
                namaterpanjang = ngitung_panjang_matriks(str(data_game_yang_dimiliki[i][1])) + 2
            if ngitung_panjang_matriks(str(data_game_yang_dimiliki[i][2])) > kategoriterpanjang:
                kategoriterpanjang = ngitung_panjang_matriks(str(data_game_yang_dimiliki[i][2])) + 2
            if ngitung_panjang_matriks(str(data_game_yang_dimiliki[i][3])) > tahunterpanjang: 
                tahunterpanjang = ngitung_panjang_matriks(str(data_game_yang_dimiliki[i][3])) + 2
            if ngitung_panjang_matriks(str(data_game_yang_dimiliki[i][4])) > hargaterpanjang:
                hargaterpanjang = ngitung_panjang_matriks(str(data_game_yang_dimiliki[i][4])) + 2  
        
        for i in range(0,ngitung_panjang_matriks(data_game_yang_dimiliki)):   
            print(f"  {data_game_yang_dimiliki[i][0]}  ",end=" "*  (idterpanjang - ngitung_panjang_matriks(str(data_game_yang_dimiliki[i][0]))))
            print(f"|",end="  ")
            print(f"{data_game_yang_dimiliki[i][1]}",end=" "* (namaterpanjang - ngitung_panjang_matriks(str(data_game_yang_dimiliki[i][1]))))
            print("|",end="  ")
            print(f"{data_game_yang_dimiliki[i][2]}",end=" "* (kategoriterpanjang - ngitung_panjang_matriks(str(data_game_yang_dimiliki[i][2]))))
            print("|",end="  ")
            print(f"{data_game_yang_dimiliki[i][3]}",end=" " * (tahunterpanjang - ngitung_panjang_matriks(str(data_game_yang_dimiliki[i][3]))))
            print("|",end="  ")
            print(f"{data_game_yang_dimiliki[i][4]}")  
# -----------------------------------------------------------------------------------


#F10 - Mencari Game yang dimiliki dari ID dan Tahun Rilis ---------------------------
def search_my_game(kepemilikantemp,userID,mtrxgametemp):
    #Prosedur akan mencetak game yang dimiliki oleh user yang sesuai dengan parameter searching
    #I.S Menerima userID, matriks kepemilikan game, dan matriks game yang terdapat di toko
    #F.S. Mencetak game yang dimiliki oleh user yang sesuai dengan parameter searching

    #KAMUS LOKAL
    #id_game_yang_dimiliki,kepemilikantemp,mtrxgametemp,datagameyangdimiliki: array of array of string and integer
    #filtered_game,filtered_game_temp: array of array of string and integer
    #id_game,tahun_rilis: string 
    #idterpanjang,namaterpanjang,kategoriterpanjang,hargaterpanjang,tahunterpanjang,jumlah_game_filtered: integer

    #Deklarasi Fungsi/Prosedur
    # function ngitung_panjang_matriks (matriks : array of array of string) -> integer
    # Menghitung banyaknya data dalam bentuk array pada matriks

    #ALGORITMA
    id_game_yang_dimiliki = []
    for i in range(ngitung_panjang_matriks(kepemilikantemp)): #Memasukkan id game yang dimiliki ke dalam matriks id_game_yang_dimiliki
        if kepemilikantemp[i][1] == userID :
            id_game_yang_dimiliki += [kepemilikantemp[i][0]]
    
    data_game_yang_dimiliki = []
    for i in range(ngitung_panjang_matriks(mtrxgametemp)): #Memasukkan data game yang dimiliki sesuai dengan data yang terdapat pada id_game_yang_dimiliki
        for j in range(ngitung_panjang_matriks(id_game_yang_dimiliki)):
            if mtrxgametemp[i][0] == id_game_yang_dimiliki[j]:
                data_game_yang_dimiliki += [mtrxgametemp[i]]

    filtered_game = []
    filtered_game_temp = []
    for i in data_game_yang_dimiliki: #Mengcopy data_game_yang_dimiliki ke dalam filtered_game
        filtered_game += [i]

    
    id_game = input("Masukkan ID game: ").upper()
    if id_game != "": #Jika input tidak string kosong maka akan memasukkan game yang dimiliki ke dalam filtered game temp jika sesuai dengan parameter
        for i in filtered_game:
            if i[0] == id_game:
                filtered_game_temp += [i]
        filtered_game = filtered_game_temp #Mengubah filtered game menjadi filtered_game_temp
        filtered_game_temp = []

    tahun_rilis = input("Masukkan tahun rilis: ") 
    while tahun_rilis != "" and not tahun_rilis.isdigit(): #Melakukan validasi input apakah input merupakan angka atau tidak
        print("Tolong berikan masukkan yang valid!")
        tahun_rilis = input("Masukkan tahun rilis: ")
    if tahun_rilis != "": #Jika input tidak string kosong maka akan memasukkan game yang dimiliki ke dalam filtered game temp jika sesuai dengan parameter
        for i in filtered_game:
            if i[3] == int(tahun_rilis):
                filtered_game_temp += [i]
        filtered_game = filtered_game_temp #Mengubah filtered_game menjadi filtered_game_temp

    print("")
    print("Daftar game pada toko yang memenuhi kriteria:")
    
    idterpanjang = 7
    namaterpanjang = 0
    kategoriterpanjang = 0
    tahunterpanjang = 0
    hargaterpanjang = 0

    if filtered_game == []: #Jika tidak ada yang memenuhi kriteria filter
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
    else: #Mencetak fitlered matrix yang sudah diproses
        filtered_game = [["ID","NAMA","KATEGORI","TAHUN","HARGA","STOK"]] + filtered_game
        jumlah_game_filtered = ngitung_panjang_matriks(filtered_game)
        
        for i in range(jumlah_game_filtered): #Looping untuk menghitung kata terpanjang dari setiap data elemen filtered_game
            if ngitung_panjang_matriks(str(filtered_game[i][1])) > namaterpanjang:
                namaterpanjang = ngitung_panjang_matriks(str(filtered_game[i][1])) + 2
            if ngitung_panjang_matriks(str(filtered_game[i][2])) > kategoriterpanjang:
                kategoriterpanjang = ngitung_panjang_matriks(str(filtered_game[i][2])) + 2
            if ngitung_panjang_matriks(str(filtered_game[i][3])) > tahunterpanjang: 
                tahunterpanjang = ngitung_panjang_matriks(str(filtered_game[i][3])) + 2
            if ngitung_panjang_matriks(str(filtered_game[i][4])) > hargaterpanjang:
                hargaterpanjang = ngitung_panjang_matriks(str(filtered_game[i][4])) + 2         

        for i in range(0,jumlah_game_filtered):   
            print(f"  {filtered_game[i][0]}  ",end=" "*  (idterpanjang - ngitung_panjang_matriks(str(filtered_game[i][0]))))
            print(f"|",end="  ")
            print(f"{filtered_game[i][1]}",end=" "* (namaterpanjang - ngitung_panjang_matriks(str(filtered_game[i][1]))))
            print("|",end="  ")
            print(f"{filtered_game[i][2]}",end=" "* (kategoriterpanjang - ngitung_panjang_matriks(str(filtered_game[i][2]))))
            print("|",end="  ")
            print(f"{filtered_game[i][3]}",end=" " * (tahunterpanjang - ngitung_panjang_matriks(str(filtered_game[i][3]))))
            print("|",end="  ")
            print(f"{filtered_game[i][4]}")
# -----------------------------------------------------------------------------------

#F11 - Mencari Game di Toko ---------------------------------------------------------
def search_game_at_store(mtrxgametemp):
    #Fungsi akan mencetak game di toko yang sesuai dengan parameter searching
    #I.S. Menerima parameter berupa matrix yang terdapat dalam toko
    #F.s. Mengeluarkan output game yang sesuai dengan parameter searching

    #KAMUS LOKAL
    #filtered_matrix,mtrxgametemp,filtered_matrix_temp: array of array of string and integer
    #idterpanjang,namaterpanjang,kategoriterpanjang,tahunterpanjang,hargaterpanjang,stokterpanjang,panjang_matrix: integer
    #gameid,nama,kategori,harga_game,tahun_rilis: string

    #Deklarasi Fungsi/Prosedur
    # function ngitung_panjang_matriks (matriks : array of array of string) -> integer
    # Menghitung banyaknya data dalam bentuk array pada matriks

    #ALGORITMA
    filtered_matrix = []
    for i in range(1,ngitung_panjang_matriks(mtrxgametemp)): #Mengcopy data dari mtrxgametemp ke dalam filtered_matrix
        filtered_matrix += [mtrxgametemp[i]]
    filtered_matrix_temp = []
    panjang_matrix = ngitung_panjang_matriks(filtered_matrix)
    
    gameid = input("Masukkan ID Game: ").upper() #Menerima input game id yang akan di filter
    if gameid != "": 
        for i in range(panjang_matrix): #Looping untuk mengecek apakah ada id yang sesuai dengan input
            if filtered_matrix[i][0] == gameid:
                filtered_matrix_temp += [filtered_matrix[i]]
        filtered_matrix = filtered_matrix_temp
        filtered_matrix_temp = []
        panjang_matrix = ngitung_panjang_matriks(filtered_matrix)

    nama = input("Masukkan Nama Game: ").upper() #Menerima input nama game yang akan di filter
    if nama != "":
        for i in range(panjang_matrix): #Looping untuk mengecek apakah ada nama yang sesuai dengan input
            if filtered_matrix[i][1].upper() == nama:
                filtered_matrix_temp += [filtered_matrix[i]]
        filtered_matrix = filtered_matrix_temp
        filtered_matrix_temp = []
        panjang_matrix = ngitung_panjang_matriks(filtered_matrix)
    
    harga_game = input("Masukkan harga: ")
    
    while not harga_game.isdigit() and harga_game != "": #Looping sampai mendapatkan input integer/string kosong
        print("Tolong berikan masukkan yang valid!")
        harga_game = input("Masukkan harga: ")
    
    if harga_game != "": #Menerima input harga game yang akan di filter
        for i in range(panjang_matrix): #Looping untuk mengecek apakah ada harga game yang sesuai dengan input
            if filtered_matrix[i][4] == int(harga_game):
                filtered_matrix_temp += [filtered_matrix[i]]
        filtered_matrix = filtered_matrix_temp
        filtered_matrix_temp = []
        panjang_matrix = ngitung_panjang_matriks(filtered_matrix)

    kategori = input("Masukkan kategori game: ").upper() #Menerima input kategori game yang akan di filter
    if kategori != "":
        for i in range(panjang_matrix):  #Looping untuk mengecek apakah ada kategori yang sesuai dengan input
            if filtered_matrix[i][2].upper() == kategori:
                filtered_matrix_temp += [filtered_matrix[i]]
        filtered_matrix = filtered_matrix_temp
        filtered_matrix_temp = []
        panjang_matrix = ngitung_panjang_matriks(filtered_matrix)

    tahun_rilis = input("Masukkan tahun rilis: ")
    
    while not tahun_rilis.isdigit() and tahun_rilis != "": #Looping sampai mendapatkan input tahun_rilis integer/string kosong
        print("Tolong berikan masukkan yang valid!")
        tahun_rilis = input("Masukkan tahun rilis: ")
    
    if tahun_rilis != "": 
        for i in range(panjang_matrix): #Looping untuk mengecek apakah ada tahun rilis yang sesuai dengan input
            if filtered_matrix[i][3] == int(tahun_rilis):
                filtered_matrix_temp += [filtered_matrix[i]]
        filtered_matrix = filtered_matrix_temp
        panjang_matrix = ngitung_panjang_matriks(filtered_matrix)
    
    print("")
    print("Daftar game pada toko yang memenuhi kriteria:")
    
    idterpanjang = 7
    namaterpanjang = 0
    kategoriterpanjang = 0
    tahunterpanjang = 0
    hargaterpanjang = 0
    stokterpanjang = 0
    
    if filtered_matrix == []: #Jika tidak ada yang memenuhi kriteria filter
        print("Tidak ada game pada toko yang memenuhi kriteria")
    else: #Mencetak fitlered matrix yang sudah diproses
        filtered_matrix = [["id","nama","kategori","tahun","harga","stok"]] + filtered_matrix
        jumlah_game_filtered = ngitung_panjang_matriks(filtered_matrix)
        for i in range(jumlah_game_filtered): #Looping untuk menghitung kata terpanjang dari setiap data elemen filtered_matrix
            if ngitung_panjang_matriks(str(filtered_matrix[i][1])) > namaterpanjang:
                namaterpanjang = ngitung_panjang_matriks(str(filtered_matrix[i][1])) + 2
            if ngitung_panjang_matriks(str(filtered_matrix[i][2])) > kategoriterpanjang:
                kategoriterpanjang = ngitung_panjang_matriks(str(filtered_matrix[i][2])) + 2
            if ngitung_panjang_matriks(str(filtered_matrix[i][3])) > tahunterpanjang: 
                tahunterpanjang = ngitung_panjang_matriks(str(filtered_matrix[i][3])) + 2
            if ngitung_panjang_matriks(str(filtered_matrix[i][4])) > hargaterpanjang:
                hargaterpanjang = ngitung_panjang_matriks(str(filtered_matrix[i][4])) + 2
            if ngitung_panjang_matriks(str(filtered_matrix[i][5])) > stokterpanjang:
                stokterpanjang = ngitung_panjang_matriks(str(filtered_matrix[i][5])) + 2     
        for i in range(0,jumlah_game_filtered):   
            print(f"  {filtered_matrix[i][0]}  ",end=" "*  (idterpanjang - ngitung_panjang_matriks(str(filtered_matrix[i][0]))))
            print(f"|",end="  ")
            print(f"{filtered_matrix[i][1]}",end=" "* (namaterpanjang - ngitung_panjang_matriks(str(filtered_matrix[i][1]))))
            print("|",end="  ")
            print(f"{filtered_matrix[i][2]}",end=" "* (kategoriterpanjang - ngitung_panjang_matriks(str(filtered_matrix[i][2]))))
            print("|",end="  ")
            print(f"{filtered_matrix[i][3]}",end=" " * (tahunterpanjang - ngitung_panjang_matriks(str(filtered_matrix[i][3]))))
            print("|",end="  ")
            print(f"{filtered_matrix[i][4]}",end=" " * (hargaterpanjang - ngitung_panjang_matriks(str(filtered_matrix[i][4]))))
            print("|",end="  ")
            print(f"{filtered_matrix[i][5]}")
# -----------------------------------------------------------------------------------

#F12 - Topup Saldo ------------------------------------------------------------------
def topup(isAdmin,usertemp):
    #Fungsi akan menambahkan saldo ke akun user yang diinginkan
    #I.S. Array of Array of string and integer
    #F.S. Array of Array of string and integer

    #KAMUS LOKAL
    #isAdmin,angkavalid: boolean
    #usertemp: array of array of string and integer
    #username,operation: string
    #index,sisa_saldo,saldo: integer

    #Deklarasi Fungsi/Prosedur
    # function ngitung_panjang_matriks (matriks : array of array of string) -> integer
    # Menghitung banyaknya data dalam bentuk array pada matriks

    #ALGORITMA
    if not isAdmin: #Jika bukan admin
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
    else: #Jika Admin
        username = input("Masukkan username: ").upper()
        angka_valid = False
        while not angka_valid: #Melakukan validasi input apakah integer atau tidak dan akan diulangi sampai mendapatkan input integer
            try:
                saldo = int(input("Masukkan jumlah: "))
            except ValueError:
                print("Tolong berikan masukkan yang valid!")
                continue
            else:
                angka_valid = True
        if saldo < 0: #Mengecek apakah saldo dikurangi atau tidak
            operation = "dikurangi"
        else: 
            operation = "ditambahkan"
        index = 0
        ada = False
        for i in range(ngitung_panjang_matriks(usertemp)): #Mengecek apakah ada user yang sesuai dengan input
            if usertemp[i][1].upper() == username:
                ada = True
                sisa_saldo = int(usertemp[i][5]) + saldo 
                index = i
        if ada: #Ada user dengan username input
            if sisa_saldo >= 0: #Jika hasil akhir saldo >= 0 maka saldo akan diubah
                usertemp[index][5] = str(sisa_saldo)
                print(f"Saldo user {usertemp[index][1]} berhasil {operation}. Saldo Sekarang {sisa_saldo}")
                return usertemp #Mengemablikan usertemp yang sudah diubah
            else: #Jika hasil akhir saldo < 0 maka saldo tidak akan diubah
                print(f"Saldo user {usertemp[index][1]} gagal {operation}. Saldo Sekarang {usertemp[index][5]} (<{-1*saldo})")
                return usertemp #Mengembalikan usertemp inisial
        else: #Tidak ada user dengan username input
            print("Tidak ada user dengan username tersebut!")
            return usertemp #Mengembalikan usertemp inisial
# -----------------------------------------------------------------------------------

#F13 - Melihat Riwayat Pembelian ----------------------------------------------------
def riwayat(userID,riwayattemp):
    #Prosedur akan mencetak game yang telah dibeli oleh user
    #I.S. Menerima input matrix riwayat pembelian game
    #F.S. Mengeluarkan output game yang telah dibeli oleh user

    #KAMUS LOKAL
    #game_yang_dimiliki,riwayattemp: array of array of string and integer
    #userID: string
    #idterpanjang,namaterpanjang,hargaterpanjang,tahunterpanjang: integer

    #Deklarasi Fungsi/Prosedur
    # function ngitung_panjang_matriks (matriks : array of array of string) -> integer
    # Menghitung banyaknya data dalam bentuk array pada matriks

    #ALGORITMA
    game_yang_dimiliki = []
    for i in range(ngitung_panjang_matriks(riwayattemp)): #Memasukkan game yang telah dibeli oleh user ke dalam matrix game_yang_dimiliki
        if userID == riwayattemp[i][3]:
            game_yang_dimiliki += [riwayattemp[i]]
    
    idterpanjang = 7
    namaterpanjang = 0
    hargaterpanjang = 0
    tahunterpanjang = 0
    game_yang_dimiliki = [["ID","Nama","Harga","User ID","Tahun Beli"]] + game_yang_dimiliki

    for i in range(ngitung_panjang_matriks(game_yang_dimiliki)): #Looping untuk menghitung kata terpanjang dari setiap data elemen game_yang_dimiliki
        if ngitung_panjang_matriks(str(game_yang_dimiliki[i][1])) > namaterpanjang:
            namaterpanjang = ngitung_panjang_matriks(str(game_yang_dimiliki[i][1])) + 2
        if ngitung_panjang_matriks(str(game_yang_dimiliki[i][4])) > tahunterpanjang: 
            tahunterpanjang = ngitung_panjang_matriks(game_yang_dimiliki[i][4]) + 2
        if ngitung_panjang_matriks(str(game_yang_dimiliki[i][2])) > hargaterpanjang:
            hargaterpanjang = ngitung_panjang_matriks(str(game_yang_dimiliki[i][2])) + 2  
    
    print("Daftar game:")
    if game_yang_dimiliki == []: #Jika tidak ada yang memenuhi kriteria filter
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah buy_game untuk membeli")
    else: #Mencetak game_yang_dimiliki yang sudah diproses
        for i in range(0,ngitung_panjang_matriks(game_yang_dimiliki)):   
            print(f"  {game_yang_dimiliki[i][0]}  ",end=" "*  (idterpanjang - ngitung_panjang_matriks(str(game_yang_dimiliki[i][0]))))
            print(f"|",end="  ")
            print(f"{game_yang_dimiliki[i][1]}",end=" "* (namaterpanjang - ngitung_panjang_matriks(str(game_yang_dimiliki[i][1]))))
            print("|",end="  ")
            print(f"{game_yang_dimiliki[i][2]}",end =" "*(hargaterpanjang- ngitung_panjang_matriks(str(game_yang_dimiliki[i][2]))))
            print("|",end="  ")
            print(f"{game_yang_dimiliki[i][4]}")
# -----------------------------------------------------------------------------------

#F14 - Help -------------------------------------------------------------------------
def help():
    # Menampilkan keyword-keyword yang tersedia ke layar
    
    # I.S. sembarang
    # F.S. tercetak list keyword help ke layar
    
    # KAMUS LOKAL

    # ALGORITMA
    if isAdmin:
        print("""
============================================================ HELP ============================================================
\033[1mregister\033[0m              | melakukan registrasi user baru                                                    
\033[1mlogin\033[0m                 | melakukan login ke dalam sistem                                                        
\033[1mtambah_game\033[0m           | menambah game yang dijual pada toko                                               
\033[1mubah_game\033[0m             | mengubah game pada toko                                                           
\033[1mubah_stok\033[0m             | mengubah stok sebuah game pada toko                                               
\033[1mlist_game_toko\033[0m        | melihat list game yang ada di toko                                                     
\033[1msearch_game_at_store\033[0m  | mencari game di toko berdasarkan ID, nama game, harga, kategori, dan tahun rilis       
\033[1mtopup\033[0m                 | menambah saldo kepada user                                                        
\033[1msave\033[0m                  | menyimpan data setelah dilakukan perubahan                                             
\033[1mhelp\033[0m                  | memberikan panduan penggunaan sistem                                                   
\033[1mexit\033[0m                  | keluar dari aplikasi                                                                   
            """)
    
    else:
        print("""
============================================================ HELP ============================================================
\033[1mlogin\033[0m                 | melakukan login ke dalam sistem                                                        
\033[1mlist_game_toko\033[0m        | melihat list game yang ada di toko                                                     
\033[1mbuy_game\033[0m              | membeli game dan memasukkan ke dalam list game user                              
\033[1mlist_game\033[0m             | melihat game yang dimiliki oleh user                              
\033[1msearch_my_game\033[0m        | mencari game yang dimiliki berdasarkan ID dan tahun rilis                        
\033[1msearch_game_at_store\033[0m  | mencari game di toko berdasarkan ID, nama game, harga, kategori, dan tahun rilis       
\033[1mriwayat\033[0m               | melihat riwayat pembelian game                                                   
        """)
# -----------------------------------------------------------------------------------

#F15 - Load -------------------------------------------------------------------------
def CobaUbah(data):
    # Mengubah tipe data yang ada pada data menjadi boolean atau integer jika dimungkinkan
    # I.S. data terdefinisi
    # F.S. dikembalikan data dimana elemen yang dapat diubah, diubah menjadi boolean atau integer telah diubah
    
    # KAMUS LOKAL
    # i, j : integer

    #Deklarasi Fungsi/Prosedur
    # function len_manual (string : string) -> integer
    # Menghitung jumlah karakter/huruf pada string
    
    # ALGORITMA
    for i in range(len_manual(data)):
        for j in range(len_manual(data[i])):
            try:
                # Dicoba diubah menjadi integer
                data[i][j] = int(data[i][j])
            except:
                ValueError
            # Dicoba diubah menjadi boolean
            if data[i][j] == "True":
                data[i][j] = True
            elif data[i][j] == "False":
                data[i][j] = False
    return data

def load(folder):
    # Membaca file-file csv pada folder yang diinputkan
    # I.S. pada folder terdapat file-file csv yang dibutuhkan
    # F.S. didapatkan matriks data sesuai dengan file-file csv yang ada

    # KAMUS LOKAL
    # user : array of data_user
    # game : array of data_game 
    # kepemilikan : array of data_kepemilikan
    # riwayat : array of data_riwayat 

    # Variable global
    global game
    global kepemilikan
    global riwayat_beli
    global user

    # Function / Procedure
    # load_data(file : csv) -> array of array of string
    # Membaca file csv dan mengembalikan matriks data sesuai data csv
    # I.S. file terdefinisi
    # F.S. dikembalikan matriks data sesuai file

    # CobaUbah(data : array of array of string)
    # Mengubah tipe data yang ada pada data menjadi boolean atau integer jika dimungkinkan
    # I.S. data terdefinisi
    # F.S. dikembalikan data dimana elemen yang dapat diubah, diubah menjadi boolean atau integer telah diubah

    # ALGORITMA
    os.chdir('./' + str(folder))

    user = CobaUbah(csv_pars(open("user.csv",'r').read()))
    game = CobaUbah(csv_pars(open("game.csv",'r').read()))
    kepemilikan = CobaUbah(csv_pars(open("kepemilikan.csv").read()))
    riwayat_beli = CobaUbah(csv_pars(open("riwayat.csv",'r').read()))
    os.chdir('../')

def loading():
    # Membaca argumen dari python menggunakan argparse
    # I.S. sembarang
    # F.S. Dikembalikan driectory folder csv jika ada, dan None jika tidak ada
    
    # KAMUS LOKAL
    # parser : ArgumentParser
    # directory, parent, path, files : string
    # lstFile : array of string

    # Function / Procedure
    # fileExist(files : csv) -> boolean
    # Mengecek apakah file ada atau tidak
    # I.S. sembarang
    # F.S. Dikembalikan True jika file ada, dan False jika tidak ada
    
    # ALGORITMA
    # Penjelasan program
    parser = argparse.ArgumentParser()
    
    # Menghandle jika input salah
    parser.add_argument("-f","--folder", type=str, help="Input nama folder csv (harus diinput! )")
    if parser.parse_args().folder is None:
        parser.error("""
\033[91m Nama folder csv tidak diinput! \033[0m
\033[93m format input : python program.py -f <nama-folder-csv> \033[0m""")
        return None
    
    # Berpindah directory ke folder csv
    directory = parser.parse_args().folder
    parent = os.getcwd()
    path = os.path.join(parent, directory)
    
    # Validasi folder ada
    if not os.path.exists(path):
        print("Nama folder yang diinputkan tidak ada")
    else:
        os.chdir('./' + directory)
        lstFile = ["game.csv","kepemilikan.csv","riwayat.csv","user.csv"]
        for files in lstFile:
            # Validasi file ada
            if not fileExist(files):
                print(files + " tidak tersedia di folder yang diinputkan")
                return None
        # Berpindah directory ke parent
        os.chdir('../')
        return directory
        
def fileExist(files):
    # Mengecek apakah file ada atau tidak
    # I.S. sembarang
    # F.S. Dikembalikan True jika file ada, dan False jika tidak ada
    
    # KAMUS LOKAL
    
    # ALGORITMA
    if os.path.exists(files):
        return True
    else:
        return False
# -----------------------------------------------------------------------------------

#F16 - Save -------------------------------------------------------------------------
def convert_matrix_to_string(datas) :
# Matriks user diubah ke bentuk strings sesuai dengan format data csv.

    # KAMUS LOKAL
    # data_string : string
    # data, i : integer

    # Deklarasi fungsi/prosedur
    # function slicing (string : string) -> string
    # Menghapus karakter terakhir pada string

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
        data_string = slicing(data_string)
        # Jika sudah terhapus, maka prosedur akan pindah ke baris berikutnya dan mengulang langkah-langkah di atas untuk array berikutnya.
        data_string += "\n"

    return data_string

def save_data(data, filename) :
# Data yang sudah diperbarui akan disimpan ke file data.

    # KAMUS LOKAL
    
    # Deklarasi fungsi/prosedur
    # function convert_matrix_to_string (datas : array of array of string) -> string
    # Matriks user diubah ke bentuk strings sesuai dengan format data csv.

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

    # Deklarasi fungsi/prosedur
    # function save_data (data, filename : string)
    # Data yang sudah diperbarui akan disimpan ke file data.
    
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
    save_data(riwayat_beli, "riwayat.csv")
    save_data(kepemilikan, "kepemilikan.csv")

    print("Data telah tersimpan pada folder " + folder_name + "!")
    os.chdir("../")         # Prosedur kembali ke folder asal (supaya tidak berada di dalam folder penyimpanan)
# -----------------------------------------------------------------------------------

# F17 - Exit ------------------------------------------------------------------------
def exit():
# I.S. Program masih melakukan looping untuk meminta input command;
# F.S. Program berhenti melakukan looping
    
    # KAMUS LOKAL
    # confirm_save : string

    # Deklarasi fungsi/prosedur
    # procedure save()
    # I.S. Matriks user, game, riwayat, dan kepemilikan terdefinisi; F.S. Data user, game, riwayat, dan kepemilikan tersimpan dalam bentuk file csv dan disimpan di folder sesuai dengan input user.

    # ALGORITMA
    # Menerima input untuk mengonfirmasi penyimpanan data.
    confirm_save = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    # Melakukan validasi terhadap input yang diterima, yaitu Y atau N baik dalam huruf besar maupun huruf kecil.
    while confirm_save.upper() != "Y" and confirm_save.upper() != "N":
        # Jika inputnya tidak valid, maka prosedur akan meminta input ulang sampai didapatkan input yang benar.
        confirm_save = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    # Jika pengguna ingin menyimpan perubahan pada BNMO, maka prosedur akan memanggil prosedur save() dan melakukan penyimpanan data.
    if confirm_save.upper() == "Y":
        save()

# -----------------------------------------------------------------------------------


# Main Program ----------------------------------------------------------------------
isAdmin = False
notLogin = True
user = []
game = []
kepemilikan = []
riwayat_beli = []


folder = loading()

if folder != None:
    print("Loading...")
    print("")
    print("""\`
    
\033[1m  ██╗       ██╗███████╗██╗      █████╗  █████╗ ███╗   ███╗███████╗⠀  \033[0m\033[36m⠀⢀⡤⠶⠶⠖⠒⠒⠒⠛⠛⠛⠉⠉⠉⠉⠉⠉⠉⠉⠉⢻⣿⣿⣷⣶⣦⣤⣤⣤⣀⣀⠀⠀⠀⠀⠀\033[0m
\033[1m  ██║  ██╗  ██║██╔════╝██║     ██╔══██╗██╔══██╗████╗ ████║██╔════╝   \033[0m\033[36m ⣾⠀⢀⡤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⣄⠀  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀ \033[0m
\033[1m  ╚██╗████╗██╔╝█████╗  ██║     ██║  ╚═╝██║  ██║██╔████╔██║█████╗     \033[0m\033[36m⠀⡇ ⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⢸⠀⠀ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀\033[0m
\033[1m   ████╔═████║ ██╔══╝  ██║     ██║  ██╗██║  ██║██║╚██╔╝██║██╔══╝⠀⠀   \033[0m\033[36m⠀⡇⠀⡇⠀\033[91m⠠⠒⡀⠀⠀⠀⠀  ⢀⠒. \033[36m⢸⠀⠀ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀\033[0m
\033[1m   ╚██╔╝ ╚██╔╝ ███████╗███████╗╚█████╔╝╚█████╔╝██║ ╚═╝ ██║███████╗⠀  \033[0m\033[36m⠀⡇⠀⡇⠀\033[91m⠀⠀⠀⣄    ⣠⠀ ⠀⠀\033[36m⢸⠀⠀ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀\033[0m
\033[1m    ╚═╝   ╚═╝  ╚══════╝╚══════╝ ╚════╝  ╚════╝ ╚═╝     ╚═╝╚══════╝⠀  \033[0m\033[36m⠀⡇⠀⡇⠀\033[91m⠀⠀⠀⠀⠉⠉⠉⠉⠀ ⠀\033[36m⠀ ⢸⠀  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀\033[0m
\033[1m                         ████████╗ █████╗                        ⠀⠀  \033[0m\033[36m⠀⡇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⢸⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀ \033[0m
\033[1m                         ╚══██╔══╝██╔══██╗                       ⠀⠀  \033[0m\033[36m⠀⡇⠀⠙⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠒⠋⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀\033[0m
\033[1m                            ██║   ██║  ██║                       ⠀⠀  \033[0m\033[36m⠀⡇⠀⠀⣤⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⣠⣤⣄⠀⠀  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀\033[0m
\033[1m                            ██║   ██║  ██║                       ⠀⠀  \033[0m\033[36m⠀⡇⠀⠀⠛⠛⠛⠛⠛⠛⠃⠀⠀⠀⠀⠙⠿⠋⠀  ⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀      \033[0m  
\033[1m                            ██║   ╚█████╔╝                       ⠀  \033[0m\033[36m ⣸⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀\033[0m
\033[1m                            ╚═╝    ╚════╝                        ⠀  \033[0m\033[36m⢰⣿⠀⠀ ⡏ ⡇⠀⠀⠀⠀⠀ ⢸⡁⠱⣄ ⠀⠀ ⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀\033[0m
\033[1m              ██████╗ ███╗  ██╗███╗   ███╗ █████╗ ██╗            ⠀  \033[0m\033[36m⠰⡙⠒⠒⠋⢀⡾⠀⠀⠀⠀⠀⠀  ⠙⣄⡉⠛⠒⠛⠉⣁⣀⢀⣀⣀⣉⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀ \033[0m
\033[1m              ██╔══██╗████╗ ██║████╗ ████║██╔══██╗██║            ⠀  \033[0m\033[36m ⠉⡟⠓⠂⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠟⠉⠉⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀\033[0m
\033[1m              ██████╦╝██╔██╗██║██╔████╔██║██║  ██║██║             \033[0m\033[36m⢀⠤⡀⢹⡀⠀⠘⠛⣃⡛⠛⠂⠀⠀⠀⠀⠀⠙⠛⠛⠁⠀⠀⠀⣿⣿⣿⣿⡿⠿⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀ \033[0m
\033[1m              ██╔══██╗██║╚████║██║╚██╔╝██║██║  ██║╚═╝             \033[0m\033[36m⢸ ⠘⠤⠟⠛⢛⣿⠛⡻⠻⡛⢒⡲⠶⠶⠶⢶⣶⠖⠒⠒⠶⠚⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m
\033[1m              ██████╦╝██║ ╚███║██║ ╚═╝ ██║╚█████╔╝██╗             \033[0m\033[36m⠀⠙⠒⠒⠛⠉⠁⠀ ⢇⣀⣉⣉⣠⠤⠒⠚⠉⠁⠀⠀                          \033[0m
\033[1m              ╚═════╝ ╚═╝  ╚══╝╚═╝     ╚═╝ ╚════╝ ╚═╝            \033[0m
""")
    load(folder)
    berjalan = True
    selesai = False

    print("Mohon untuk login terlebih dahulu")
    while berjalan:
        if notLogin:
            print("#------------------------------------------------#")
            print("1.Login")
            print("2.Exit")
            perintah = input(">>> ")
            if perintah.lower() == "login":
                login()
            elif perintah.lower() == "save":
                save()
            elif (perintah.lower() == "tambah_game" or perintah.lower() == "ubah_game" or perintah.lower() == "ubah_stok" or perintah.lower() =="list_game_toko" or perintah.lower() == "buy_game" or 
                perintah.lower() == "list_game" or perintah.lower() == "search_my_game" or perintah.lower() == "search_game_at_store" or perintah.lower() == "topup" or 
                perintah.lower() == "help" or perintah.lower() == "riwayat" or perintah.lower() == "register"):
                print("Mohon untuk masuk ke account terlebih dahulu!")
            elif perintah.lower() == "exit":
                exit()
                break
            else:
                print("Tolong masukkan perintah yang valid!")
        else:
            print("#------------------------------------------------#")
            perintah = input(">>> ")
            if perintah.lower() == "login":
                print("Maaf kamu sudah login. \nMohon untuk keluar terlebih dahulu.")
            elif perintah.lower() == "register":
                if isAdmin:
                    register()
                else:
                    print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
            elif perintah.lower() == "tambah_game":
                game = tambah_game(game,isAdmin)
            elif perintah.lower() == "ubah_game":
                game = ubah_game(game,isAdmin)
            elif perintah.lower() == "ubah_stok":
                game = ubah_stok(game,isAdmin)
            elif perintah.lower() == "list_game_toko":
                list_game_toko(game)
            elif perintah.lower() == "buy_game":
                if not isAdmin:
                    beli_game(game,riwayat_beli,kepemilikan)
                else:
                    print("Maaf hanya user yang dapat membeli game.")
            elif perintah.lower() == "list_game":
                if not isAdmin:
                    list_game(userID,kepemilikan,game)
                else:
                    print("Maaf hanya user yang dapat melihat list game yang dimiliki.")
            elif perintah.lower() == "search_my_game":
                if not isAdmin:
                    search_my_game(kepemilikan,userID,game)
                else:
                    print("Maaf hanya user yang dapat melihat list game yang dimiliki.")
            elif perintah.lower() == "search_game_at_store":
                search_game_at_store(game)
            elif perintah.lower() == "topup":
                topup(isAdmin,user)
            elif perintah.lower() == "riwayat":
                if not isAdmin:
                    riwayat(userID,riwayat_beli)
                else:
                    print("Maaf hanya user yang dapat melihat riwayat pembeliannya.")
            elif perintah.lower() == "help":
                help()
            elif perintah.lower() == "save":
                save()
            elif perintah.lower() == "exit":
                exit()
                break
            else:
                print("Tolong berikan perintah yang valid!")
    print("""
\033[1m
    ▀█▀ █▀▀ █▀█ █ █▀▄▀█ ▄▀█   █▄▀ ▄▀█ █▀ █ █ █   █▀ █ █ █▀▄ ▄▀█ █ █
     █  ██▄ █▀▄ █ █ ▀ █ █▀█   █ █ █▀█ ▄█ █ █▀█   ▄█ █▄█ █▄▀ █▀█ █▀█

█▀▄▀█ █▀▀ █▄ █ █▀▀ █▀▀ █ █ █▄ █ ▄▀█ █▄▀ ▄▀█ █▄ █   █▄▄ █▄ █ █▀▄▀█ █▀█ █  
█ ▀ █ ██▄ █ ▀█ █▄█ █▄█ █▄█ █ ▀█ █▀█ █ █ █▀█ █ ▀█   █▄█ █ ▀█ █ ▀ █ █▄█ ▄ 
\033[0m
""")    