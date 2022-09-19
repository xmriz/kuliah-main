def ngitung_line_csv(csv):
    #Menghitung jumlah line yang terdapat pada csv file
    
    #Kamus Lokal
    #lines,i: integer

    #ALGORITMA
    lines = 0
    for i in csv: #Looping sepanjang file csv untuk menghitung jumlah line
        if i == "\n": #Jika menemukan "\n" line += 1
            lines +=1
    return(lines) #Mengembalikan jumlah line yang ada di file csv
    
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

