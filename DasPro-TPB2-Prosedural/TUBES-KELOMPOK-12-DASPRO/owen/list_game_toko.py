import functions

def list_game_toko(mtrxgametemp):
    #Mencetak game yang terdapat di toko dengan urutan sesuai input
    #I.S. Matriks data game yang terdapat di toko
    #F.S. Matriks data yang terdapat di toko dengan urutan sesuai input

    #KAMUS LOKAL
    #sorted_matrix: array of array
    #skema_sortig: string
    #panjang_matrix,i,j: integer
    #valid: boolean

    #ALGORITMA
    sorted_matrix = mtrxgametemp
    skema_sorting = input("Skema sorting: ").upper()
    panjang_matrix = functions.len_buatan(sorted_matrix)
    valid = False

    if skema_sorting == "TAHUN-": #Melakukan bubble sort untuk mengurutkan berdasarkan tahun secara descending (menurun)
        valid = True
        for i in range(1,panjang_matrix-1): 
            for j in range(1,panjang_matrix-i):
                if sorted_matrix[j][3] < sorted_matrix[j+1][3]:
                    sorted_matrix[j+1],sorted_matrix[j] = sorted_matrix[j],sorted_matrix[j+1]
    
    elif skema_sorting == "TAHUN+": #Melakukan bubble sort untuk mengurutkan berdasarkan tahun secara ascending (meningkat)
        valid = True
        for i in range(1,panjang_matrix-1):
            for j in range(1,panjang_matrix-i):
                if sorted_matrix[j][3] > sorted_matrix[j+1][3]:
                    sorted_matrix[j+1],sorted_matrix[j] = sorted_matrix[j],sorted_matrix[j+1]

    elif skema_sorting == "HARGA-": #Melakukan bubble sort untuk mengurutkan berdasarkan harga secara descending (menurun)
        valid = True
        for i in range(1,panjang_matrix-1):
            for j in range(1,panjang_matrix-i):
                if sorted_matrix[j][4] < sorted_matrix[j+1][4]:
                    sorted_matrix[j+1],sorted_matrix[j] = sorted_matrix[j],sorted_matrix[j+1]

    elif skema_sorting == "HARGA+": #Melakukan bubble sort untuk mengurutkan berdasarkan harga secara ascending (meningkat)
        valid = True
        for i in range(1,panjang_matrix-1):
            for j in range(1,panjang_matrix-i):
                if sorted_matrix[j][4] > sorted_matrix[j+1][4]:
                    sorted_matrix[j+1],sorted_matrix[j] = sorted_matrix[j],sorted_matrix[j+1]

    elif skema_sorting == "": #melakukan bubble sort untuk mengurutkan berdasarkan game id secara ascending (meningkat)
        valid = True
        for i in range(1,panjang_matrix-1):
            for j in range(1,panjang_matrix-i):
                if sorted_matrix[j][0] > sorted_matrix[j+1][0]:
                    sorted_matrix[j+1],sorted_matrix[j] = sorted_matrix[j],sorted_matrix[j+1] 
                
    else: #Melakukan pengecekan apakah skema sorting valid atau tidak
        valid = False
    
    idterpanjang = 9
    namaterpanjang = 0
    kategoriterpanjang = 0
    tahunterpanjang = 0
    hargaterpanjang = 0
    stokterpanjang = 0
    
    for i in range(panjang_matrix):
        if functions.len_buatan(sorted_matrix[i][1]) > namaterpanjang:
            namaterpanjang = functions.len_buatan(sorted_matrix[i][1]) + 2
        if functions.len_buatan(sorted_matrix[i][2]) > kategoriterpanjang:
            kategoriterpanjang = functions.len_buatan(sorted_matrix[i][2]) + 2
        if functions.len_buatan(sorted_matrix[i][3]) > tahunterpanjang: 
            tahunterpanjang = functions.len_buatan(sorted_matrix[i][3]) + 2
        if functions.len_buatan(sorted_matrix[i][4]) > hargaterpanjang:
            hargaterpanjang = functions.len_buatan(sorted_matrix[i][4]) + 2
        if functions.len_buatan(sorted_matrix[i][5]) > stokterpanjang:
            stokterpanjang = functions.len_buatan(sorted_matrix[i][5]) + 2
            
    if valid: #Jika skema sorting valid akan mencetak list game pada toko sesuai dengan pilihan sorting
        for i in range(0,panjang_matrix):   
            print(f"  {sorted_matrix[i][0]}  ",end=" "*  (idterpanjang - functions.len_buatan(sorted_matrix[i][0]) ))
            print(f"|",end="  ")
            print(f"{sorted_matrix[i][1]}",end=" "* (namaterpanjang - functions.len_buatan(sorted_matrix[i][1])))
            print("|",end="  ")
            print(f"{sorted_matrix[i][2]}",end=" "* (kategoriterpanjang - functions.len_buatan(sorted_matrix[i][2])))
            print("|",end="  ")
            print(f"{sorted_matrix[i][3]}",end=" " * (tahunterpanjang - functions.len_buatan(sorted_matrix[i][3])))
            print("|",end="  ")
            print(f"{sorted_matrix[i][4]}",end=" " * (hargaterpanjang - functions.len_buatan(sorted_matrix[i][4])))
            print("|",end="  ")
            print(f"{sorted_matrix[i][5]}")
            
                      
    else: #Jika skema sorting tidak valid akan mencetak skema sorting tidak valid
        print("Skema sorting tidak valid!")