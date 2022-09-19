def get_max(arr, index_start):
  maxi = arr[index_start]
  for i in range(index_start+1,len(arr)):
      if maxi < arr[i]:
          maxi = arr[i]
  return maxi      

def get_idx(arr, number):
   for i in range(len(arr)):
       if arr[i] == number:
           return i

def swap(array, indeks_1, indeks_2):
  array[indeks_1], array[indeks_2] = array[indeks_2], array[indeks_1]

def sort(arr):
  for i in range(len(arr)):
    maxArr = get_max(arr, i)
    maxIdx = get_idx(arr, maxArr)
    swap(arr, i, maxIdx)
  print(arr)


N = int(input())
arr = [0 for i in range(N)]

for i in range(N):
    arr[i] = int(input())    

sort(arr)