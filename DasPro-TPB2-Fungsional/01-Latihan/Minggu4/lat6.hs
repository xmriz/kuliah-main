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



-- DEFINI DAN SPESIFIKASI
splitList:: [Int] -> ([Int],[Int])
{- splitList li menghasilkan 2 list of integer, list
pertama memuat bilangan positif dan 0 yang merupakan
elemen dari li (dengan urutan kemunculan yang tidak
berubah), sedangkan list kedua memuat bilangan negatif
elemen li.
Prekondisi: li mungkin kosong -}

-- REALISASI
splitList l 
    | isEmpty l = ([],[])
    | otherwise =
        let (l1,l2) = splitList (tail l)
        in
            if head l >= 0 then 
                (konso (head l) l1, l2)
            else (l1,konso (head l) l2)