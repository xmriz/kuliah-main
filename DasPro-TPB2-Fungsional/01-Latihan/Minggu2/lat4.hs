-- MENCARI NILAI TENGAH         nilaiTengah(a,b,c)

-- DEFINISI DAN SPESIFIKASI
nilaiTengah :: Int -> Int -> Int -> Int
    {- nilaiTengah (a,b,c) akan mengambil nilai tengah di antara 3 buah integer berlainan (a,b,c) setelah diurutkan -}
max3 :: Int -> Int -> Int -> Int
    {- menghasilkan nilai maksimum di antara 3 buah integer (a,b,c) -}
min3 :: Int -> Int -> Int -> Int
    {- menghasilkan nilai minimum di antara 3 buah integer (a,b,c) -}

-- REALISASI
max3 a b c
    | a>b =
        if a>c then a
        else c -- c>a>b
    | otherwise =
        if b>c then b
        else c

min3 a b c
    | a<b =
        if a<c then a
        else c -- c<a<b
    | otherwise =
        if b<c then b
        else c

nilaiTengah a b c = (a + b + c - (min3 a b c) - (max3 a b c))

-- APLIKASI
-- nilaiTengah 1 2 3