n = int(input())
list = []

for i in range(n):
    list += [int(input())]

x = int(input())

if x in list:
    hasil = 'N#A'
    if x == max(list):
        hasil = 'maksimum'
    if x == min(list):
        hasil = 'minimum'
    if (x == max(list) == min(list)):
        hasil = 'maksimum\nminimum'
    print(hasil)
else:
    print(x, 'tidak ada')
