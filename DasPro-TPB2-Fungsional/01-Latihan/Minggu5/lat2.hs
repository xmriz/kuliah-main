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

-- DEFINISI DAN SPESIFIKASI
isGenap :: Int -> Bool
-- isGenap l true jika semua elemen list of Int l genap
gtThan5 :: Int -> Bool
-- gtThan5 l true jika semua elemen list of Int l lebih dari 5

sumInteger :: Int -> Int -> (Int -> Bool) -> Int
-- sumInteger m n f menghasilkan jumlah semua angka dari m s.d. n yang memenuhi syarat f
-- prekondisi : m <= n

-- REALISASI
isGenap x = mod x 2 == 0
gtThan5 x = x > 5

sumInteger m n f
    | m == n = 
        if (f m) then m else 0
    | otherwise = 
        if (f m) then m + sumInteger (m+1) n f
        else sumInteger (m+1) n f

-- APLIKASI
-- sumInteger 1 100 (\x -> mod 100 x == 0) , hasil = 217
-- sumInteger 1 100 (\x -> if mod x 2 == 0 then mod x 10 == 0 else mod x 5 == 0) , hasil = 1050
-- sumInteger 25 25 (\x -> x < 10), hasil = 0