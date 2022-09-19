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

-- offset : perubahan nilai terhadap elemen dalam list

-- FUNGSI OFFSET

-- DEFINISI DAN SPESIFIKASI
plus2 :: Int -> Int
    {- menambahkan tiap elemen dengan 2 -}
minus1 :: Int -> Int
    {- mengurangi tiap elemen dengan 1 -}
offKond :: Int -> Int
    {- akan menghasilkan list baru dengan nilai setiap elemen yang diubah sesuai ketentuan range tertentu -}

-- REALISASI
plus2 x = x + 2
minus1 x = x - 1
offKond x
    | x >= 0 && x <= 40 = 10
    | x < 0 = 0
    | x > 40 = 20

-- DEFINISI DAN SPESIFIKASI
offsetList :: [Int] -> (Int->Int) -> [Int]
    {- menerima list of integer dan fungsi offset -}

-- REALISASI
offsetList l offset
    | isEmpty l = []
    | otherwise = konso (offset (head l)) (offsetList (tail l) offset) 


-- APLIKASI
-- offsetList [1,2,3,4] plus2 atau offsetList [1,2,3,4] (\x -> x+2) 