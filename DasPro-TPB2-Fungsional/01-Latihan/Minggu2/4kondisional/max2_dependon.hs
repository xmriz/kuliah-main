-- MAXIMUM          max2(a,b)

-- DEFINISI DAN SPESIFIKASI
max2 :: Int -> Int -> Int
    {-mencari nilai maximum dari dua nilai-}

-- REALISASI
max2 a b 
    | a>=b = a
    | otherwise = b -- a<b

-- APLIKASI
-- max2 3 4 