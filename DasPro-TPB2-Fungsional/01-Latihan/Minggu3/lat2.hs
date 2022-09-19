-- BILANGAN GANJIL          isGanjil(x)

-- DEFINISI DAN SPESIFIKASI
isGanjil :: Int -> Bool 
    {- isGanjil(x) merupakan suatu predikat untuk memeriksa apakah sebuah bilangan integer (>=0) merupakan bilangan ganjil -}

-- REALISASI
isGanjil x
    | x == 0 = False --basis
    | x == 1 = True 
    | otherwise = isGanjil (x-2)  --rekurens

-- APLIKASI
-- isGanjil 11