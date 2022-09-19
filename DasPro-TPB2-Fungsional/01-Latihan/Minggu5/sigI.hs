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
sigI :: Int -> Int -> Int
    {- menghitung sigma i pada interval a sampai b, dengan beda 1 -}
sigI3 :: Int -> Int -> Int
    {- menghitung sigma i^3 pada interval a sampai b, dengan beda 1 -}
sp8 :: Int -> Int -> Float
    {- menghitung sigma 1/(i*(i+2)) -}

-- REALISASI
sigI a b 
    | a > b = 0
    | otherwise = a + (sigI (a+1) b)

sigI3 a b
    | a > b = 0
    | otherwise = a^3 + (sigI3 (a+1) b)

sp8 a b
    | a > b = 0
    | otherwise =  (1/fromIntegral(a*(a+2))) + (sp8 (a+4) b)



-- ==================================================================================================

-- DEFINISI DAN SPESIFIKASI
id :: Int -> Int
    {- mengirimkan nilai i -}
p1 :: Int -> Int
    {- mengirimkan nilai i+1 -}
p4 :: Int -> Int
    {- mengirimkan nilai i+4 -}
cube :: Int -> Int
    {- mengirimkan nilai i^3 -}
t :: Int -> Float
    {- mengirimkan nilai 1/(i(i+2)) -}

sigma :: Int -> Int -> (Int -> Float) -> (Int -> Int) -> Float
    {- begitulah yah.. -}

-- REALISASI, bisa juga pakai ekspresi lambda
id i = i
p1 i = i+1
p4 i = i+4
cube i = i^3
t i = 1/fromIntegral(i*(i+2))

sigma a b f s
    | a > b = 0
    | otherwise = (f a) + (sigma (s a) b f s)


-- APLIKASI
