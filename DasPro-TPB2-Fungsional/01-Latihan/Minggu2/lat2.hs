-- KONVERSI WAKTU             jumlahDetik(j,m,d)

-- DEFINISI DAN SPESIFIKASI
jumlahDetik :: Int -> Int -> Int -> Int
    {- diberikan 3 buah integer yang menunjukan jam(j) menit(m) detik(d) 
    jumlahDetik j m d akan menghitung jumlah detik dari jam tersebut -}

-- REALISASI
jumlahDetik j m d = 
    (j*3600) + (m*60) + d

-- APLIKASI
-- jumlahDetik 12 30 45