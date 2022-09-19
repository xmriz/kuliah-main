import pandas as pd
import fungsimesin as fm
import datetime


#deklarasi tanggal dan waktu saat ini
waktu = datetime.datetime.now()

#deklarasi tipe data per kolom dataframe
dtype_dic = {'username': str,
            'PIN': str
}

#inisialisasi dataframe
df = pd.read_csv("data.csv", index_col="username", dtype=dtype_dic)
tries = 0
user = ""

#Penyocokan username dengan yang ada di database
print('======= LOGIN =======')
while (user not in df["PIN"]):
    user = input("Masukkan username anda: ")
    if (user not in df["PIN"]):
        print("Username anda tidak valid. Silahkan coba lagi.")

#Autentikasi PIN
while (tries < 3):
    try:
        pin = int(input("Masukkan PIN: "))
        if (str(pin) == df.loc[user][0]):
            break
        else:
            raise KeyError
    except KeyError:
        if (tries < 2):
            print("PIN anda salah. Coba lagi. (" + str(2-tries) + " percobaan lagi).")
        else:
            print(f"User {user} terblokir. Silahkan hubungi admin yang sah.")
            fm.userblock(user)
            exit()
        tries += 1

#Menu Utama
me = 0
while True:
    me = fm.menu()
    if me == 1:
        #Pilihan menu pertama, menjalankan program struk belanja
        from food import Food
        from drink import Drink
        
        print('=====================')

        food1 = Food('Seblak', 5000, 330)    #membuat instance untuk class Food
        food2 = Food('Batagor', 4000, 450)
        food3 = Food('Kue Sus', 2000, 180)

        foods = [food1, food2, food3]

        drink1 = Drink('Kopi', 3000, 180)        #membuat instance untuk class Food
        drink2 = Drink('Jus Jeruk', 5000, 350)
        drink3 = Drink('Es Oyen', 3500, 300)

        drinks = [drink1, drink2, drink3]

        print('MAKANAN')
        index = 0
        for food in foods:
            print(str(index) + '. ' + food.info())
            index += 1
        print('MINUMAN')
        index = 0
        for drink in drinks:
            print(str(index) + '. ' + drink.info())
            index += 1

        print('=====================')

        pembeli = input("Masukkan nama Pembeli: ")

        print('=====================')

        food_order = int(input('Ingin beli makanan apa?: '))
        while food_order < 0 or food_order >= len(foods):
            print('Makanan yang ada pilih tidak berada dalam menu. Silahkan pilih lagi.')
            food_order = int(input('Ingin beli makanan apa?: '))
        selected_food = foods[food_order]

        print('=====================')

        drink_order = int(input('Ingin beli minuman apa?: '))
        while drink_order < 0 or drink_order >= len(drinks):
            print('Makanan yang ada pilih tidak berada dalam menu. Silahkan pilih lagi.')
            drink_order = int(input('Ingin beli makanan apa?: '))
        selected_drink = drinks[drink_order]

        print('=====================')

        print('Anda akan membeli ' + selected_food.name + ' dan ' + selected_drink.name)

        count = int(input('Mau beli berapa paket makanan dan minuman(diskon 10% jika beli lebih dari 3)?: '))
        
        isDiskon = 'Tidak'
        if count > 3:
            isDiskon = 'Ya'
        
        result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)
        print('Harga total adalah ' + str(fm.formatrupiah(result)) + ',00')

        print('=====================')
        uang = int(input('Berapa jumlah uang yang anda gunakan untuk membayar?: Rp'))
        fm.wait(1.1)
        if uang >= result:
            date = f'{waktu.day}/{waktu.month}/{waktu.year}'
            time = f'{waktu.hour:02}.{waktu.minute:02}'
            # Mencetak struk beli
            print(f'''\nOutput :
            =================================                                         
            ------ S T R U K  B E L I ------                
            -------- (9  R E S T O) --------
            =================================
            Date              : {date}
            Time              : {time}
            Staff             : {user}
            =================================
            Nama              : {pembeli}
            Makanan           : {selected_food.name}
            Minuman           : {selected_drink.name}
            Jumlah paket      : {count}
            =================================
            Diskon 10%        : {isDiskon}
            =================================
            Total             : {fm.formatrupiah(result) + ',00'}
            Bayar             : {fm.formatrupiah(uang) + ',00'}
            =================================
            Kembali           : {fm.formatrupiah(uang-result) + ',00'}
            =================================
            ---  T E R I M A  K A S I H  ---
            =================================
            ''')
            # menambahkan data pembelian ke database
            fm.sendto(date, time, pembeli, user, result)
        else:
            print('Uang yang anda miliki tidak cukup. Coba lagi nanti.')

        if (fm.prompt() == 0):
            break
    elif me == 2:
        print('=====================')
        #Pilihan menu kedua, ganti PIN
        pinbaru = input("Masukkan PIN baru: ")
        fm.gantiPIN(user, pinbaru)
        if (fm.prompt() == 0):
            break
    elif me == 3:
        print('=====================')
        #Pilihan menu ketiga, tambah Admin
        useradm = input('Masukkan username admin baru: ')
        pinadm = input('Masukkan PIN dari admin baru: ')
        fm.tambahadmin(useradm, pinadm)
        if (fm.prompt() == 0):
            break
    elif me == 4:
        print('=====================')
        #Pilihan menu keempat, cek total pemasukan keseluruhan
        fm.ceksaldo()
        if (fm.prompt() == 0):
            break
    else:
        print('=====================')
        #Bila nomor menu tidak valid
        print("Nomor menu tidak valid.")
        if (fm.prompt() == 0):
            break