def InputValidasi(r1,r2,r3,jenis):
    cons = True
    benar = ['s','S', 'p', 'P']

    if (r1 <= 0) or (r2 <= 0) or (r3 <= 0):
        cons = False
    if not (jenis in benar):
        cons = False
         
    if not cons:
        print("Masukan salah")
        return False
    else: 
        return True

def HasilHitung(r1,r2,r3,jenis):
    if (jenis == 's') or (jenis == 'S'):
        hasil = r1 + r2 + r3
        return ("%.2f" % hasil)
    else: 
        hasil = 1/((1/r1) + (1/r2) + (1/r3))
        return ("%.2f" % hasil)


lanjut = False
while not lanjut:
    r1 = float(input())
    r2 = float(input())
    r3 = float(input())
    jenis = input()

    lanjut = InputValidasi(r1,r2,r3,jenis)

print(HasilHitung(r1,r2,r3,jenis))