import functions

def tambah_game(mtrxgametemp):
    #Menambahkan game baru pada matriks game csv

    #KAMUS LOKAL
    #jumlahdata,tahun_rilis,harga_game,stok_awal: integer
    #nama_game,kategori_game,gameid: integer

    #ALGORITMA
    jumlah_data = functions.len_buatan(mtrxgametemp)
    if jumlah_data < 10: #Memberikan game id pada game baru yang akan ditambahkan
        gameid = "GAME00" + str(jumlah_data)
    elif 10 <= jumlah_data < 100:
        gameid = "GAME0" + str(jumlah_data)
    else:
        gameid = "GAME" + str(jumlah_data)

    nama_game = input("Masukkan nama game: ")

    kategori_game = input("Masukkan kategori game: ")

    while True: #Melakukan validasi input apakah integer terhadap tahun rilis game. Akan meminta input sampai mendapatkan input integer
        try:
            tahun_rilis = input("Masukkan tahun rilis: ")
            if tahun_rilis != "":
                tahun = int(tahun_rilis)
        except ValueError:
            print("Tolong berikan masukkan yang valid!")
            continue
        else:
            break
    
    while True: #Melakukan validasi input apakah integer terhadap harga game. Akan meminta input sampai mendapatkan input integer
        try:
            harga_game = input("Masukkan harga: ")
            if harga_game != "":
                harga = int(harga_game)
        except ValueError:
            print("Tolong berikan masukkan yang valid!")
            continue
        else:
            break

    while True:  #Melakukan validasi input apakah integer terhadap stok awal game. Akan meminta input sampai mendapatkan input integer
        try:
            stok_awal = input("Masukkan stok awal: ")
            if stok_awal != "":
                stok = int(stok_awal)
        except ValueError:
            print("Tolong berikan masukkan yang valid!")
            continue
        else:
            break
    
    while nama_game == "" or kategori_game == "" or tahun_rilis == "" or harga_game == "" or stok_awal == "": 
        #Mengecek apakah ada input yang kosong atau tidak dan akan diulangi sampai semua input terisi 
        print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
        nama_game = input("Masukkan nama game: ")
        kategori_game = input("Masukkan kategori game: ")
        while True: #Melakukan validasi input apakah integer terhadap tahun rilis game. Akan meminta input sampai mendapatkan input integer
            try:
                tahun_rilis = input("Masukkan tahun rilis: ")
                if tahun_rilis != "":
                    tahun = int(tahun_rilis)
            except ValueError:
                print("Tolong berikan masukkan yang valid!")
                continue
            else:
                break
        
        while True: #Melakukan validasi input apakah integer terhadap harga game. Akan meminta input sampai mendapatkan input integer
            try:
                harga_game = input("Masukkan harga: ")
                if harga_game != "":
                    harga = int(harga_game)
            except ValueError:
                print("Tolong berikan masukkan yang valid!")
                continue
            else:
                break

        while True: #Melakukan validasi input apakah integer terhadap stok awal game. Akan meminta input sampai mendapatkan input integer
            try:
                stok_awal = input("Masukkan stok awal: ")
                if stok_awal != "":
                    stok = int(stok_awal)
            except ValueError:
                print("Tolong berikan masukkan yang valid!")
                continue
            else:
                break
    
    else: #Jika semua input sudah terisi akan menambahkan game baru ke dalam matriks game
        print(f"Selamat! Berhasil menambahkan game {nama_game}")
        gamebaru = [gameid,nama_game,kategori_game,tahun_rilis,harga_game,stok_awal]
        return mtrxgametemp + [gamebaru] #Mengembalikan matriks game yang terdapat di toko baru yang sudah di update
        
