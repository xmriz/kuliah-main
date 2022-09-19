import tulisdata

def insertionSort(arr):
    for Pass in range(1, len(arr)):
        Temp = arr[Pass]
        i = Pass-1
        while i >=0 and Temp[0] < arr[i][0]:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = Temp

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

    insertionSort(lst)
    for i in range(len(lst)):
        print(lst[i][0],end=",")
        print(lst[i][1].rstrip(),end=',')
        print(lst[i][2])
        
f.close()