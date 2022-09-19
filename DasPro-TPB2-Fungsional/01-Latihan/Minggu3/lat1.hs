-- DERET SEGITIGA           deretSegitiga(n)

-- DEFINISI DAN SPESIFIKASI
deretSegitiga :: Int -> Int 
    {- deretSegitiga(n) merupakan fungsi untuk mencari nilai bilangan ke-n pada deret segitiga.
    Deret segitiga : 1, 3, 6, 10, 15, .. -}

-- REALISASI
deretSegitiga n
    | n == 1 = 1
    | otherwise = deretSegitiga (n-1) + n

-- APLIKASI 
-- deretSegitiga 5