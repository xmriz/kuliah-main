-- MAXIMUM 3            max3(a,b,c)

-- DEFINISI DAN SPESIFIKASI
max3 :: Int -> Int -> Int -> Int
    {- mencari nilai maximum dari 3 bilangan-}

-- REALISASI
max3 a b c
    | a>b =
        if a>c then a
        else c -- c>a>b
    | otherwise =
        if b>c then b
        else c