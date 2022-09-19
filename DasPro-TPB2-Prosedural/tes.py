array = [1,2,3,4,6,7,8,9,10]

i = 0
while (i <= (len(array)-1)) and (array[i] != 5):
    i += 1
if (array[i] == 5):
    print(f'Found 5 at index {i}')
else:
    print('Not found 5')
    