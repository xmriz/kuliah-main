-- MO           mo(a,b,c,d)

-- DEFINISI DAN SPESIFIKASI
mo :: Int -> Int -> Int -> Int -> Float
    {- mo(a, b, c, d) menghasilkan nilai rata-rata 
    dari dua di antara a, b, c, d dengan mengabaikan
    nilai terbesar dan nilai terkecil -}
max4 :: Int -> Int -> Int -> Int -> Int
    {- max4(a, b, c, d) menghasilkan nilai maksimum
    di antara a, b, c, d-}
min4 :: Int -> Int -> Int -> Int -> Int
    {- min4(a, b, c, d) menghasilkan nilai minimum
    di antara a, b, c, d-}
max2 :: Int -> Int -> Int
    {- max2(a, b) menghasilkan nilai maksimum di
    antara a, b -}
min2 :: Int -> Int -> Int
    {- min2(a, b) menghasilkan nilai minimum di
    antara a, b -}

-- REALISASI
-- versi dengan "abstraksi"
max2 a b = div (a+b + abs(a-b)) 2
min2 a b = div (a+b - abs(a-b)) 2
max4 a b c d = max2 (max2 a b) (max2 c d)
min4 a b c d = min2 (min2 a b) (min2 c d)
mo a b c d = fromIntegral(a+b+c+d - (max4 a b c d) - (min4 a b c d))/2
-- fungsi di dalam fromIntegralI(Int) tidak bisa pakai /, soalnya nilai didalam fromIntegral harus Int, jadi harus pakai div
-- fromIntegral casting Int to Float, agar sesuai definisi masukan berupa integer dan output berupa float

-- APLIKASI
-- mo 1 2 3 4