import datetime
waktu = datetime.datetime.now()

print("~~~~Program Kasir Sederhana Ekorkode~~~~")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

total1=0
jenis1=""
porsi=0
gelas=0

def fungsimakanan():
   global total1
   global porsi
   global jenis1
   print ("\n~~~~Menu Makanan~~~~")
   print("1. Nasi Goreng - Rp15000")
   print("2. Soto - Rp9000")
   print("3. Mie Ayam - Rp11000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       total1=porsi*15000
       print (porsi," porsi Nasi Goreng Telur = Rp", total1)
       jenis1=("Nasi Goreng")
   elif nomor==2:
       total1=porsi*9000
       print (porsi," porsi Soto = Rp", total1)
       jenis1=("Soto")
   elif nomor==3:
       total1=porsi*11000
       print (porsi, " porsi Mie Ayam = Rp", total1)
       jenis1=("Mie Ayam")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()


fungsimakanan()

total2=0
jenis2=""

def fungsiminuman():
   global total2
   global jenis2
   global gelas
   print("\n~~~~Menu Minuman~~~~")
   print("1. Es teh - Rp2000")
   print("2. Es jeruk - Rp3500")
   print("3. Es kopi - Rp4000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       total2=gelas*2000
       print (gelas," Es Teh = Rp", total2)
       jenis2=("Gelas Es Teh")
   elif nomor==2:
       total2=gelas*3500
       print (gelas, " Gelas Es Jeruk = Rp", total2)
       jenis2=("Es Jeruk")
   elif nomor==3:
       total2=gelas*4000
       print (gelas, " Gelas Es Kopi = Rp", total2)
       jenis2=("Es Kopi")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()


fungsiminuman()
    
totalsemua=0
totalsemua=total1+total2
print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp."))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n===========================")
print("--- S T R U K   B E L I ---")
print("----- (9 R E S T O) -----")
print("===========================")
print(f' {waktu.day}/{waktu.month}/{waktu.year}           {waktu.hour}.{waktu.minute}')
print (" Staff        :",pembeli)
print("===========================")
print (" Nama         :",pembeli)
print (" Beli         :",porsi,jenis1,"-", total1)
print ("               ",gelas,jenis2,"-", total2)
print("===========================")
print (" Subtotal     : Rp.",totalsemua)
print (" Diskon       : Rp.",totalsemua)
print("===========================")
print (" Total        : Rp.",totalsemua)
print (" Uang         : Rp.",uang)
print("===========================")
print (" Kembali      : Rp.",kembalian)
print("===========================")
print("  T E R I M A  K A S I H  ")
print("===========================")

