a = int(input("Masukkan banyaknya baris: "))
b = int(input("Masukkan banyaknya kolom: "))

m = [[0 for j in range(b)] for i in range(a)]
sum = 0

for i in range(a):
    for j in range(b):
        m[i][j] = int(input(f"elemen {[i,j]} : "))

for i in range(a):
    for j in range(b):
        sum += m[i][j]

print(f"Nilai rata-rata elemen matriks = {sum/(a*b)}")

c = int(input("Indeks baris yang dihapus = "))
d = int(input("Indeks kolom yang dihapus = "))

print("submatriks yaitu")
for i in range(a):
    for j in range(b):
        
        if i == c or j == d:
            pass
        else:
            print(m[i][j], end=" ")
    if i == c or j == d:
        pass

    else:
        print()

num = 0
for i in range(a):
    for j in range(b):
        if i == c or j == d:
            pass
        else:
            num += m[i][j]

print(f"Nilai rata-rata elemen submatriks = {(num/((a-1)*(b-1)))}")