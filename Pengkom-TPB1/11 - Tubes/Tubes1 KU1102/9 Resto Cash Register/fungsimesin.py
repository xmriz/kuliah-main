import pandas as pd
import time
from csv import DictWriter

def menu():
    # Mencetak menu pilihan ke layar dan menerima input pilihan dari pengguna
    
    # KAMUS LOKAL
    # menu : int
    
    # ALGORITMA
    print('''
=====================
╔═══╗╔═══╗     ╔╗
║╔═╗║║╔═╗║    ╔╝╚╗
║╚═╝║║╚═╝╠══╦═╩╗╔╬══╗
╚══╗║║╔╗╔╣║═╣══╣║║╔╗║
╔══╝║║║║╚╣║═╬══║╚╣╚╝║
╚═══╝╚╝╚═╩══╩══╩═╩══╝
=====================
    Pilih menu:
    1. Pembelian
    2. Ganti PIN
    3. Tambah Admin
    4. Total Pemasukan''')
    menu = int(input("Pilih nomor menu: "))
    return menu

def wait(t):
    # Menahan waktu dengan jumlah detik sesuai argumen
    
    # KAMUS LOKAL
    # i, t : integer
    
    # ALGORITMA
    print("Silahkan tunggu...")
    time.sleep(t)

def prompt():
    # Memberi pilihan kepada pengguna apakah akan melanjutkan pemakaian atau tidak
    
    # KAMUS LOKAL
    # ask : string
    
    # ALGORITMA
    print('=====================')
    ask = input("Apakah anda ingin menjalankannya lagi? (y/n): ")
    if (ask == 'y'):
        return 1
    else:
        print('=====================')
        print("Terima kasih telah menggunakan Mesin Kasir ini.")
        return 0

def formatrupiah(nilai):
    # Mengubah penulisan nilai menjadi penulisan nominal angka rupiah yang benar
    
    # KAMUS LOKAL
    # nilai : int
    
    # ALGORITMA
    y = str(nilai)
    if len(y) <= 3:
        return 'Rp' + y
    else :
        p = y[-3:]
        q = y[:-3]
        return formatrupiah(q) + '.' + p

def gantiPIN(user, pinbaru):
    # Mengganti pin ATM pengguna untuk autentikasi berikutnya
    
    # KAMUS LOKAL
    # user, pinbaru : str
    
    # ALGORITMA
    if(len(pinbaru) == 6 and pinbaru.isnumeric()):
        df.loc[user][0] = str(pinbaru)
        wait(1.1)
        print(f"Berhasil mengubah PIN untuk {user}.")
        df.to_csv('data.csv')
    else:
        print("PIN baru yang anda masukkan tidak valid. Coba lagi nanti.")

def tambahadmin(useradm, pinadm):
    # Menambah user pada database  beserta PIN-nya
    
    # KAMUS LOKAL
    # useradm, pinadm : str
    
    # ALGORITMA
    headerCSV = ['username', 'PIN']
    data = {'username': useradm, 'PIN' : pinadm}
    if(len(pinadm) == 6 and pinadm.isnumeric()):
        with open('data.csv', 'a', newline='') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=headerCSV)
            dictwriter_object.writerow(data)
            f_object.close()
        wait(1.1)
        print(f'{useradm} telah ditambahkan sebagai Admin.')
    else:
        print("PIN admin baru yang anda masukkan tidak valid. COba lagi nanti.")

def userblock(user):
    # Menghapus data dari user pada database
    
    # KAMUS LOKAL
    # user : str

    # ALGORITMA
    df = pd.read_csv("data.csv")
    df = df[df['username'] != user]
    df.to_csv('data.csv', index = False)

def sendto(date, time, pembeli, user, result):
    # Menambah data pembelian pada database

    # KAMUS LOKAL
    # date, time, pembeli, user : str
    # result : int

    # ALGORITMA
    dtype_dic = {'date': str,
                'time': str,
                'nama': str,
                'staff' : str,
                'pemasukan' : int
    }

    df = pd.read_csv("data_pembelian.csv", dtype=dtype_dic)
    headerCSV = ['date', 'time', 'nama', 'staff', 'pemasukan']
    data_pembelian = {'date': date, 'time' : time, 'nama' : pembeli, 'staff' : user, 'pemasukan' : result }
    with open('data_pembelian.csv', 'a', newline='') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=headerCSV)
        dictwriter_object.writerow(data_pembelian)
        f_object.close()

def ceksaldo():
    # Mencetak total seluruh pemasukan 9 Resto

    # KAMUS LOKAL
    # pemasukan : int

    # ALGORITMA
    df = pd.read_csv("data_pembelian.csv")
    saldo = df["pemasukan"].sum()
    wait(1.1)
    print(f'Total pemasukan 9 Resto adalah {formatrupiah(saldo)},00')


# inisialisasi dataframe
df = pd.read_csv("data.csv", index_col="username")