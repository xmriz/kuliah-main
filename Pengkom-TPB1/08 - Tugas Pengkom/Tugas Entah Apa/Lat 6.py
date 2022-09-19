N = int(input('masukkan jumlah hari : '))
data_suhu = []
jumlah_suhu = 0

for i in range(1, N+1):
    suhu = int(input(f'masukkan suhu hari ke{i}'))
    jumlah_suhu += suhu
    data_suhu.append(suhu)

suhu_max = max(data_suhu)
suhu_min = min(data_suhu)
rata2 = jumlah_suhu/N

print(f'suhu rata-rata : {rata2}')
print(f'suhu tertinggi : {suhu_max}')
print(f'suhu terendah : {suhu_min}')