Ric = ["Ric","HP awal","HP","Jumlah Aksi",[],"Aksi ke-"]
Kil = ["Kil","HP awal","HP","Jumlah Aksi",[],"Aksi ke-"]
VS = [Ric, Kil]
for n in range(2):
	HP = int(input("HP "+VS[n][0]+" : "))
	VS[n][1],VS[n][2]=HP,HP
	VS[n][3] = int(input("Jumlah aksi "+VS[n][0]+" : "))
	for i in range(VS[n][3]):
		ac = input("Aksi "+VS[n][0]+" ke-"+str(i+1)+" : ")
		VS[n][4] += [ac]
i = 1
VS[0][5],VS[1][5] = 0,0
while VS[0][2]>0 and VS[1][2]>0:
	if i%2 != 0:
		who = 0
		opp = 1
	else:
		who = 1
		opp = 0
		
	if VS[who][4][VS[who][5]] == "H":
		VS[who][2] += (VS[who][1]-VS[who][2])//10
	else:
		VS[opp][2] -= int(VS[who][4][VS[who][5]])
		
	if VS[who][5] == VS[who][3]-1:
		VS[who][5] = 0
	else:
		VS[who][5] += 1
	
	if (n+1)//2 >= 5:
		if (n+1)//2 >= 5:
			kutukan = 10
		else:
			kutukan += 5
		VS[0][2] -= kutukan
		VS[1][2] -= kutukan
		
	i += 1

if VS[0][2] <= 0:
	print(VS[1][0]+" menang")
else:
	print(VS[0][0]+" menang")