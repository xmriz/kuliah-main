import functions

def ubah_stok(mtrxgametemp):
    #Melakukan perubahan stok pada matriks game yang terdapat di toko
    
    #KAMUS LOKAL
    #id_yang_diubah,operation: string
    #ada: boolean
    #banyak_berubah,index,i: integer

    #ALGORITMA
    id_yang_diubah = input("Masukkan ID game: ").upper()
    ada = False
    while True: #Melakukan validasi input apakah integer atau tidak dan akan diulangi sampai mendapatkan input integer
        try:
            banyak_berubah = int(input("Masukkan jumlah: "))
        except ValueError:
            print("Tolong berikan masukkan yang valid!")
            continue
        else:
            break
    index = 0
    if banyak_berubah < 0: #Mengecek apakah game ditambah atau dikurang
        operation = "dikurangi"
    else:
        operation = "ditambahkan"
    for i in range(1,functions.len_buatan(mtrxgametemp)): #Looping untuk mencari apakah ada game dengan id sesuai input di toko
        if mtrxgametemp[i][0] == id_yang_diubah: #Jika game ada akan dilakukan perubahan stok
            ada = True
            sisa_stock = int(mtrxgametemp[i][5]) + banyak_berubah
            index = i
    
    if not ada: #Jika game tidak ada akan di mencetak tidak ada game dengan id tersebut
        print("Tidak ada game dengan ID tersebut!")
        return mtrxgametemp
    else: #Matriks akan diupdate dengan perubahan stok
        if sisa_stock >= 0: #Jika dicoba melakukan perubahan stok, stok game masih lebih besar sama dengan 0, maka matriks akan di update
            mtrxgametemp[index][5] = str(sisa_stock)
            print(f"Stok game {mtrxgametemp[index][1]} berhasil {operation}. Stok Sekarang {sisa_stock}")
            return mtrxgametemp #Mengembalikan matriks yang di update
        else: #Jika dicoba melakukan perubahan stok, stok game dibawah 0. Maka matriks tidak akan di update.
            print(f"Stok game {mtrxgametemp[index][1]} gagal {operation}. Stok Sekarang {mtrxgametemp[i][5]} (<{-1*banyak_berubah})")
            return mtrxgametemp #Mengembalikan matriks yang semula

