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
isPos :: Int -> Bool 
    {- akan menghasilkan list baru yang hanya berisi elemen list masukan yang positif -}
isNeg :: Int -> Bool 
    {- akan menghasilkan list baru yang hanya berisi elemen list masukan yang negatif -}
isKabisat :: Int -> Bool 
    {- akan menghasilkan list baru yang hanya berisi elemen list yang masuk kategori tahun kabisat -}

filterList :: [Int] -> (Int -> Bool) -> [Int]
    {- akan menghasilkan list baru yang hanya berisi elemen list masukan sesuai kondisi -}


-- REALISASI
isPos x = x >= 0
isNeg x = x < 0
isKabisat x = (mod x 4 == 0) && (mod x 100 /= 0) || (mod x 400 == 0)

filterList l f
    | isOneElmt l = 
        if f (head l) then l 
        else []
    | otherwise = 
        if f (head l) then konso (head l) (filterList (tail l) f)
        else filterList (tail l) f

-- APLIKASI
-- filterList [1,2,3,4,5,6,7,8,9,10] isPos atau
-- filterList [1,2,3,4,5,6,7,8,9,10] (\x -> x >= 0)
