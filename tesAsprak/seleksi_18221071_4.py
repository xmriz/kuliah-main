def F(x,y):
    if x == 0:
        return y+1
    elif y == 0:
        return F(x-1,1)
    else:
        return F(x-1,F(x,y-1))

x = input('Masukkan x: ')
y = input('Masukkan y: ')
print(f'Nilai F({x},{y}) = {F(int(x),int(y))}')