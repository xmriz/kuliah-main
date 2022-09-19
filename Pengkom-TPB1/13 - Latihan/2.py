kata = input('masukkan kata yang ingin di cek : ')
polindrom = True

if kata[0:int(len(kata)/2)] != kata[int(len(kata)/2):int(len(kata))]:
    polindrom = False

if polindrom == True:
    print('Ganteng!')
else:
    print('Tidak Ganteng!')