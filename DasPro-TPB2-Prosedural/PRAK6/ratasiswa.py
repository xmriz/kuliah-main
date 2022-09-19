import tulisdata

namafile = input()
tulisdata.TulisDataSiswa(namafile)

f = open(namafile,'r')
lst = []

line1 = f.readline()
if line1 == "99999999":
    print("File kosong")
else:
    while line1 != "99999999":
        line2 = f.readline()
        line3 = f.readline()
        tup = (int(line1),line2,int(line3))
        lst.append(tup)
        line1 = f.readline()

    lst.sort(key=lambda tup: tup[0])
    lst.append("mark")
    i = 0
    while lst[i] != "mark":
        nim = lst[i][0]
        CSum = 0
        CCount = 0
        while True:
            CSum += lst[i][2]
            CCount += 1
            i += 1
            if nim != lst[i][0]:
                break
        rata = ("%.2f" % round((CSum/CCount),2))
        print(str(nim) + "=" + str(rata))

f.close()