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

-- URUT GABUNGAN            mergeList(l1,l2)

-- DEFINISI DAN SPESIFIKASI
mergeList :: [Int] -> [Int] -> [Int]
{- mergeList li1 li2 menghasilkan list of integer yang
merupakan hasil penggabungan li1 dan li2, dan tetap
terurut membesar.
Prekondisi: li1 dan li2 adalah list terurut membesar
dan mungkin kosong -}

-- REALISASI
mergeList l1 l2
    | isEmpty l1 = l2
    | isEmpty l2 = l1
    | head l1 <= head l2 = konso (head l1) (mergeList (tail l1) l2)
    | otherwise = konso (head l2) (mergeList l1 (tail l2))