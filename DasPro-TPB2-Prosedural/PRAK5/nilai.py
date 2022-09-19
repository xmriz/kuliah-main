x = int(input())

if x == -9999:
    print('Data nilai kosong')
else: 
    mhs = 0
    gaklulus = 0
    lulus = 0
    sumx = 0
    while x != -9999:
        if (0 <= x <= 100):
            sumx += x
            mhs += 1
            if x < 40:
                gaklulus += 1
            else:
                lulus += 1
        x = int(input())
    
    if mhs == 0:
        print(mhs)
    else:
        print(mhs)
        print(lulus)
        print(gaklulus)
        print("%.2f" % (sumx/mhs))

