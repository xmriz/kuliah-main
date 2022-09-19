k = int(input("kelipatan : "))
s = int(input("suku : "))
a = k
n = 1
N = 0
for i in range(s):
	if i%k != 0:
		print(N*k-n,end=" ")
		n += 1
	else:
		N += 1
		print(N*k,end=" ")
		n = 1