mark = '.'

def TulisTeks():
    f = open("dataku.txt",'w')
    kalimat = input()
    f.write(kalimat) 
    f.close()

TulisTeks()
f = open("dataku.txt",'r')
c1 = f.read(1)

lst = ['A','a','I','i','U','u','E','e','O','o']
count = 0
while c1 != mark:
    if c1 in lst:
        count += 1
    c1 = f.read(1)

print (count)