N = int(input("Masukkan bilangan (N) : "))
jumlah = 0

for i in range (1, N+1)  :  
    for j in range (i+1, N+1) :
        for k in range (j+1, N+1) :
            if (i+j>k) and (j+k>i) and (k+i>j): 
                jumlah +=1
       
   
print(f"Banyaknya triplet a, b, c adalah {jumlah}")