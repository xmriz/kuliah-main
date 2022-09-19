import functions;

import os; import argparse;

# ============================ F15 ========================================
def csv_pars(csv) :
    panjang_line = ngitung_line_csv(csv)
    banyak_kolom = ngitung_kolom_csv(csv)
    file_parsed = [[0 for i in range(banyak_kolom)] for i in range(panjang_line)]
    data = 0
    while data < panjang_line:
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

def ngitung_line_csv(csv):
    #Menghitung jumlah line yang terdapat pada csv file
    
    #Kamus Lokal
    #l,i: integer

    #ALGORITMA
    l = 0
    for i in csv: #Looping sepanjang file csv untuk menghitung jumlah line
        if i == "\n": #Jika menemukan "\n" line += 1
            l +=1
    return(l) #Mengembalikan jumlah line yang ada di file csv

def ngitung_kolom_csv(csv) :
    kolom = 0
    for i in csv :
        if i == ";" :
            kolom += 1
        if i =="\n" :
            return kolom + 1
    
def gamecsv_pars(gamecsv):
    #Memisahkan game csv menjadi matriks

    #KAMUS LOKAL
    #panjangline,data,counter,j: integer
    #game_parsed: array of array
    #gamecsv,item: string

    #ALGORITMA
    panjang_line = ngitung_line_csv(gamecsv)
    game_parsed = [[0 for i in range(6)] for i in range(panjang_line)] #Membuat matriks untuk diisi dengan data dari game csv
    data = 0
    while data < panjang_line: #Looping selama line csv belum habis
        counter = 0 #Menandakan element apa pada data-X 
        item = "" #Elemen pada counter-X
        for j in gamecsv: 
            if j == "\n":  #Jika elemen merupakan "\n" akan pindah untuk mengisi elemen pada array baru
                game_parsed[data][counter] = item
                data +=1
                counter = 0
                item = ""
            elif j == ";": #Jika elemen merupakan ";" akan pindah untuk mengisi elemen pada counter baru
                game_parsed[data][counter] = item
                counter += 1
                item = ""
            else: #Jika elemen bukan ";" ataupun "\n" maka akan menyusun elemen yang akan diisi untuk counter-X
                item += j
    return(game_parsed) #Mengembalikan matriks yang sudah terbentuk dengan array berisi [id,username,nama,password,role,saldo]

def len_buatan(matriks):
    #Menghitung panjang dari matriks

    #KAMUS LOKAL
    #count,i: integer

    #ALGORITMA
    count = 0
    for i in matriks: #Looping elemen yang terdapat di matriks
        count += 1 #Setiap elemen yang ada di matriks count akan bertambah 1
    return count #Mengembalikan jumlah elemen yang terdapat di matriks

def tryChange(data):
    # Mengubah tipe data yang ada pada data menjadi boolean atau integer jika dimungkinkan
    # I.S. data terdefinisi
    # F.S. dikembalikan data dimana elemen yang dapat diubah, diubah menjadi boolean atau integer telah diubah
    
    # KAMUS LOKAL
    # i, j : integer
    
    # ALGORITMA
    for i in range(len(data)):
        for j in range(len(data[i])):
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
    global riwayat
    global user

    # Function / Procedure
    # load_data(file : csv) -> array of array of string
    # Membaca file csv dan mengembalikan matriks data sesuai data csv
    # I.S. file terdefinisi
    # F.S. dikembalikan matriks data sesuai file

    # tryChange(data : array of array of string)
    # Mengubah tipe data yang ada pada data menjadi boolean atau integer jika dimungkinkan
    # I.S. data terdefinisi
    # F.S. dikembalikan data dimana elemen yang dapat diubah, diubah menjadi boolean atau integer telah diubah

    # ALGORITMA
    os.chdir('./' + str(folder))

    user = tryChange(csv_pars("user.csv"))
    game = tryChange(gamecsv_pars("game.csv"))
    kepemilikan = tryChange(csv_pars("kepemilikan.csv"))
    riwayat = tryChange(csv_pars("riwayat.csv"))
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
    parser = argparse.ArgumentParser(description="""
Program Tugas Besar IF1210 Kelompok 12 Kelas 10 Dasar Pemrograman
\033[93m format input : python main.py -f <nama-folder-csv> \033[0m
""", epilog='Enjoy our program! :D')
    
    # Menghandle jika input salah
    parser.add_argument("-f","--folder", type=str, help="Inputkan nama folder csv (harus diinputkan)")  
    if parser.parse_args().folder is None:
        parser.error("""
\033[91m Nama folder csv tidak diinputkan! \033[0m
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
    
load()
loading()


print(user)