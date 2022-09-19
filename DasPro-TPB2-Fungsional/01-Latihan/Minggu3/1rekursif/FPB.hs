-- FPB          fpb(m,n)

-- DEFINISI DAN SPESIFIKASI
fpb :: Int -> Int -> Int
    {-mencari fpb dari dua buah bilangan-}

-- REALISASI
fpb m n
    | mod m n == 0 = n              -- basis
    | otherwise = fpb n (mod m n)   -- rekurens

-- APLIKASI
-- fpb 4 3