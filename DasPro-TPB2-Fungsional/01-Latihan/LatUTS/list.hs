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
isAllGanjil :: [Int] -> Bool
    {- isAllGanjil l true jika semua elemen list of Int l adalah ganjil
    fungsi mengembalikan True jika list kosong -}
getSmallest :: [Int] -> Int
    {- getSmallest l menghasilkan nilai terkecil dari list of Int l
    Prekondisi : l tidak kosong -}
delElement :: Int -> [Int] -> [Int]
    {- delElement x l menghasilkan list l dengan elemen x telah dihapus dari l,
    jika x bukan elemen l, maka fungsi mengembalikan l semula
    Prekondisi : elemen l unik (setiap elemen hanya muncul sekali) -}
sortList :: [Int] -> [Int]
    {- mengurutkan list dari terkecil ke terbesar . -}


-- REALISASI
isAllGanjil l
    | isEmpty l = True
    | otherwise = mod (head l) 2 /= 0 && isAllGanjil (tail l)

getSmallest l
    | isOneElmt l = head l
    | otherwise =
        if head l < getSmallest (tail l) then head l
        else getSmallest (tail l)

delElement x l
    | isEmpty l = l
    | otherwise = 
        if head l == x then delElement x (tail l)
        else konso (head l) (delElement x (tail l))

sortList l
    | isEmpty l = l
    | otherwise = konso (getSmallest l) (sortList (delElement (getSmallest l) l))


list1 :: [Int]