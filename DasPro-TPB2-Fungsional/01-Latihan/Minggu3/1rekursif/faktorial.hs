-- FAKTORIAL            fak(x)

-- DEFINISI DAN SPESIFIKASI
fak :: Int -> Int
    {-menghitung nilai faktorial dari x-}

-- REALISASI
fak x
    | x==0 = 1                      -- basis
    | otherwise = fak (x-1) * x     -- rekurens

-- APLIKASI
-- fak 5 