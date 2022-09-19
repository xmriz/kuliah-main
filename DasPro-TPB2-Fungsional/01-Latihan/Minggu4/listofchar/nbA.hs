-- DEFINISI DAN SPESIFIKASI LIST (list sudah terdefinisi di haskell) , bisa pakai definisi 2
   {- type List of Char: [ ] atau [e o List]
   Definisi type List of Char
   Basis: List of Char kosong adalah list of Char
   Rekurens: List tidak kosong dibuat dengan menambahkan sebuah elemen bertype Char di awal sebuah list atau -}


-- DEFINISI DAN SPESIFIKASI KONSTRUKTOR 1
konso :: Char -> [Char] -> [Char]
    {- konso(e,l) menghasilkan sebuah list dari e (sebuah Char) dan l (list of Char), dengan e sebagai elemen pertama : e o l -> l' -}

-- REALISASI
konso e l = [e] ++ l


-- DEFINISI DAN SPESIFIKASI SELEKTOR 1 (selektor sudah terdefinisi di haskell)
-- head :: [Char] -> Char
-- head(l) menghasilkan elemen pertama list l, l tidak kosong

-- tail :: [Char] -> [Char]
-- tail(l) menghasilkan list tanpa elemen pertama list l, l tidak kosong


-- DEFINISI DAN SPESIFIKASI PREDIKAT
isEmpty :: [Char] -> Bool
-- isEmpty l  true jika list of Char l kosong
-- REALISASI
isEmpty l = null l

isOneElmt :: [Char] -> Bool
-- isOneElmt l true jika list of Char l hanya mempunyai satu elemen
-- REALISASI
isOneElmt l = (length l) == 1


-- ==================================================================================================


-- DEFINISI DAN SPESIFIKASI
nbA :: [Char] -> Int
    {- menghitung banyak kemunculan "A" pada list of char l -}

-- REALISASI
nbA l
    | isEmpty l = 0 --basis
    | otherwise = nbA (tail l) + if head l == 'a' || head l == 'A' then 1 else 0 --rekurens
