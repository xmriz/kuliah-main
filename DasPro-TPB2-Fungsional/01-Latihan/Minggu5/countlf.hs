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

-- kondisi sebagai parameter fungsi

-- DEFINISI DAN SPESIFIKASI
isEven :: Int -> Bool
    {- menghasilkan True jika bilangan merupakan genap -}
isZero :: Int -> Bool
    {- menghasilkan True jika bilangan adalah 0 -}
isMultOf5 :: Int -> Bool
    {- menghasilkan True jika bilangan adalah kelipatan 5 -}
isCond :: Int -> Bool
    {- menghasilkan True jika memenuhi kondisi :
    - Untuk bilangan ganjil: habis dibagi 3 tapi tidak habis dibagi 5
    - Untuk bilangan genap : bernilai antara 51 hingga 100
    - sama dengan 0 -}

-- REALISASI : bisa diganti menjadi fungsi lambda
isEven x = mod x 2 == 0 -- \x -> mod x 2
isZero x = x == 0
isMultOf5 x = mod x 5 == 0
isCond x = (x == 0) || ((mod x 2 /= 0) && (mod x 3 == 0) && (mod x 5 /= 0)) || ((mod x 2 == 0) && (51 <= x) && (x <= 100))


-- DEFINISI DAN SPESIFIKASI
countlf :: [Int] -> (Int -> Bool) -> Int
    {- countlf l f menghaasilkan banyak elemen list of integer yang memenuhi kondisi yang dinyatakan dalam fungsi f -}

-- REALISASI
countlf l f
    | isEmpty l = 0
    | otherwise = 
        (if f ((head l)) then 1 else 0) + (countlf (tail l) f)

-- APLIKASI
-- countlf [1,2,3,4] isEven atau countlf [1,2,3,4] (\x -> mod x 2 == 0)