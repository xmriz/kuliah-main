-- MAXIMUM          max2(a,b)

-- DEFINISI DAN SPESIFIKASI
max2 :: Int -> Int -> Int
    {-mencari nilai maximum dari dua nilai-}

-- REALISASI
max2 a b =
    if a>=b then 
        a
    else -- a<b (else bagusnya kasih komentar)
        b

-- APLIKASI
-- max2 3 4 