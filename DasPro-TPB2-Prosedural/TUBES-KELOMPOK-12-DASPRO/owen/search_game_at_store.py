import functions

def search_game_at_store(mtrxgametemp):
    filtered_matrix = mtrxgametemp[1:]
    filtered_matrix_temp = []
    panjang_matrix = functions.len_buatan(filtered_matrix)
    
    gameid = input("Masukkan ID Game: ").upper()
    if gameid != "":
        for i in range(panjang_matrix):
            if filtered_matrix[i][0] == gameid:
                filtered_matrix_temp += [filtered_matrix[i]]
        filtered_matrix = filtered_matrix_temp
        filtered_matrix_temp = []
        panjang_matrix = functions.len_buatan(filtered_matrix)

    nama = input("Masukkan Nama Game: ").upper()
    if nama != "":
        for i in range(panjang_matrix):
            if filtered_matrix[i][1].upper() == nama:
                filtered_matrix_temp += [filtered_matrix[i]]
        filtered_matrix = filtered_matrix_temp
        filtered_matrix_temp = []
        panjang_matrix = functions.len_buatan(filtered_matrix)
    
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
    if harga_game != "":
        for i in range(panjang_matrix):
            if filtered_matrix[i][4].upper() == harga_game:
                filtered_matrix_temp += [filtered_matrix[i]]
        filtered_matrix = filtered_matrix_temp
        filtered_matrix_temp = []
        panjang_matrix = functions.len_buatan(filtered_matrix)

    kategori = input("Masukkan kategori game: ").upper()
    if kategori != "":
        for i in range(1,panjang_matrix):
            if filtered_matrix[i][2].upper() == kategori:
                filtered_matrix_temp += [filtered_matrix[i]]
        filtered_matrix = filtered_matrix_temp
        filtered_matrix_temp = []
        panjang_matrix = functions.len_buatan(filtered_matrix)

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
    if tahun_rilis != "":
        for i in range(panjang_matrix):
            if filtered_matrix[i][3].upper()== tahun_rilis:
                filtered_matrix_temp += [filtered_matrix[i]]
        filtered_matrix = filtered_matrix_temp
        panjang_matrix = functions.len_buatan(filtered_matrix)
    
    filtered_matrix = [["id","nama","kategori","tahun","harga","stok"]] + filtered_matrix
    jumlah_game_filtered = functions.len_buatan(filtered_matrix)
    
    print("Daftar game pada toko yang memenuhi kriteria:")
    
    idterpanjang = 9
    namaterpanjang = 0
    kategoriterpanjang = 0
    tahunterpanjang = 0
    hargaterpanjang = 0
    stokterpanjang = 0
    
    for i in range(jumlah_game_filtered):
        if functions.len_buatan(filtered_matrix[i][1]) > namaterpanjang:
            namaterpanjang = functions.len_buatan(filtered_matrix[i][1]) + 2
        if functions.len_buatan(filtered_matrix[i][2]) > kategoriterpanjang:
            kategoriterpanjang = functions.len_buatan(filtered_matrix[i][2]) + 2
        if functions.len_buatan(filtered_matrix[i][3]) > tahunterpanjang: 
            tahunterpanjang = functions.len_buatan(filtered_matrix[i][3]) + 2
        if functions.len_buatan(filtered_matrix[i][4]) > hargaterpanjang:
            hargaterpanjang = functions.len_buatan(filtered_matrix[i][4]) + 2
        if functions.len_buatan(filtered_matrix[i][5]) > stokterpanjang:
            stokterpanjang = functions.len_buatan(filtered_matrix[i][5]) + 2                


    if filtered_matrix == []:
        print("Tidak ada game pada toko yang memenuhi kriteria")
    else:
        for i in range(0,jumlah_game_filtered):   
            print(f"  {filtered_matrix[i][0]}  ",end=" "*  (idterpanjang - functions.len_buatan(filtered_matrix[i][0]) ))
            print(f"|",end="  ")
            print(f"{filtered_matrix[i][1]}",end=" "* (namaterpanjang - functions.len_buatan(filtered_matrix[i][1])))
            print("|",end="  ")
            print(f"{filtered_matrix[i][2]}",end=" "* (kategoriterpanjang - functions.len_buatan(filtered_matrix[i][2])))
            print("|",end="  ")
            print(f"{filtered_matrix[i][3]}",end=" " * (tahunterpanjang - functions.len_buatan(filtered_matrix[i][3])))
            print("|",end="  ")
            print(f"{filtered_matrix[i][4]}",end=" " * (hargaterpanjang - functions.len_buatan(filtered_matrix[i][4])))
            print("|",end="  ")
            print(f"{filtered_matrix[i][5]}")
