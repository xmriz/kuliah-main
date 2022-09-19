-- LUAS BUJUR SANGAKAR          luasBS(x)

-- DEFINISI DAN SPESIFKASI
luasBS :: Int -> Int 
    {- luasBS(x) merupakan fungsi untuk menghitung luas bujur sangkar dengan panjang sisi tertentu -}

-- REALISASI
luasBS x
    | x == 0 = 0 --basis
    | otherwise = luasBS (x-1) + (2*x) - 1 --rekurens

-- APLIKASI
-- luasBS 5