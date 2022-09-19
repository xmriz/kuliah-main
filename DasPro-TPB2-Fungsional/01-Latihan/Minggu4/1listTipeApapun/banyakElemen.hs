-- DEFINISI DAN SPESIFIKASI LIST (list sudah terdefinisi di haskell)
   {- type List of Int: [ ] atau [List o e]
   Definisi type List of Int
   Basis: List of Int kosong adalah list of Int
   Rekurens: List tidak kosong dibuat dengan menambahkan sebuah elemen bertype Int di akhir sebuah list atau -}


-- DEFINISI DAN SPESIFIKASI KONSTRUKTOR
konso :: Int -> [Int] -> [Int]
    {- konso(e,l) menghasilkan sebuah list dari e (sebuah Int) dan l (list of Int), dengan e sebagai elemen pertama : e o l -> l' -}

-- REALISASI
konso e l = [e] ++ l


-- DEFINISI DAN SPESIFIKASI SELEKTOR
-- last :: [Int] -> Int
-- last(l) menghasilkan elemen terakhir list l, l tidak kosong

-- init :: [Int] -> [Int]
-- init(l) menghasilkan list tanpa elemen terakhir list l, l tidak kosong


-- DEFINISI DAN SPESIFIKASI PREDIKAT
isEmpty :: [Int] -> Bool
-- isEmpty l  true jika list of Int l kosong
-- REALISASI
isEmpty l = null l

isOneElmt :: [Int] -> Bool
-- isOneElmt l true jika list of Int l hanya mempunyai satu elemen
-- REALISASI
isOneElmt l = (length l) == 1


-- ===========================================================================================

-- DEFINISI DAN SPESIFIKASI
nbElmt :: [Int] -> Int
    {- menghitung banyak elemen dari list of integer -}

-- REALISASI
nbElmt l =
    if isEmpty l then 0         -- basis
    else 1 + (nbElmt (tail l))  -- rekurens