-- DEFINISI DAN SPESIFIKASI LIST (list sudah terdefinisi di haskell) , bisa pakai definisi 2
   {- type List of Int: [ ] atau [e o List]
   Definisi type List of Int
   Basis: List of Int kosong adalah list of Int
   Rekurens: List tidak kosong dibuat dengan menambahkan sebuah elemen bertype Int di awal sebuah list atau -}


-- DEFINISI DAN SPESIFIKASI KONSTRUKTOR 1
konso :: Int -> [Int] -> [Int]
    {- konso(e,l) menghasilkan sebuah list dari e (sebuah Int) dan l (list of Int), dengan e sebagai elemen pertama : e o l -> l' -}

-- REALISASI
konso e l = [e] ++ l


-- DEFINISI DAN SPESIFIKASI SELEKTOR 1 (selektor sudah terdefinisi di haskell)
-- head :: [Int] -> Int
-- head(l) menghasilkan elemen pertama list l, l tidak kosong

-- tail :: [Int] -> [Int]
-- tail(l) menghasilkan list tanpa elemen pertama list l, l tidak kosong


-- DEFINISI DAN SPESIFIKASI PREDIKAT
isEmpty :: [Int] -> Bool
-- isEmpty l  true jika list of Int l kosong
-- REALISASI
isEmpty l = null l

isOneElmt :: [Int] -> Bool
-- isOneElmt l true jika list of Int l hanya mempunyai satu elemen
-- REALISASI
isOneElmt l = (length l) == 1


-- ==================================================================================================

-- BANYAK ELEMEN KELIPATAN 5          countMultOf5 l

-- DEFINISI DAN SPESIFIKASI
countMultOf5 :: [Int] -> Int
    {- mencari banyak elemen yang merupakan kelipatan 5 -}

-- REALISASI
countMultOf5 l
    | isEmpty l = 0
    | mod (head l) 5 == 0 = 1 + countMultOf5 (tail l)
    | otherwise = countMultOf5 (tail l)