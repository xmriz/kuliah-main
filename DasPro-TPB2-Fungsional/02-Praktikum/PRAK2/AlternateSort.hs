module AlternateSort where

-- DEFINISI DAN SPESIFIKASI LIST
{- type List of Int: [ ] atau [e o List] atau [List o e]  
   Definisi type List of Int
   Basis: List of Int kosong adalah list of Int 
   Rekurens: 
   List tidak kosong dibuat dengan menambahkan sebuah elemen bertype Int di awal 
   sebuah list atau
   dibuat dengan menambahkan sebuah elemen bertype Int di akhir sebuah list -}

-- DEFINISI DAN SPESIFIKASI KONSTRUKTOR
konso :: Int -> [Int] -> [Int]
{- konso e li menghasilkan sebuah list of integer dari e (sebuah integer) dan li 
   (list of integer), dengan e sebagai elemen pertama: e o li -> li' -}
-- REALISASI
konso e li = [e] ++ li

konsDot :: [Int] -> Int -> [Int]
{- konsDot li e menghasilkan sebuah list of integer dari li (list of integer) dan 
   e (sebuah integer), dengan e sebagai elemen terakhir: li o e -> li' -}
-- REALISASI
konsDot li e = li ++ [e]

-- DEFINISI DAN SPESIFIKASI SELEKTOR
-- head :: [Int] -> Int
-- head l menghasilkan elemen pertama list l, l tidak kosong

-- tail :: [Int] -> [Int]
-- tail l menghasilkan list tanpa elemen pertama list l, l tidak kosong

-- last :: [Int] -> Int
-- last l menghasilkan elemen terakhir list l, l tidak kosong

-- init :: [Int] -> [Int]
-- init l menghasilkan list tanpa elemen terakhir list l, l tidak kosong

-- DEFINISI DAN SPESIFIKASI PREDIKAT
isEmpty :: [Int] -> Bool
-- isEmpty l  true jika list of integer l kosong
-- REALISASI
isEmpty l = null l

isOneElmt :: [Int] -> Bool
-- isOneElmt l true jika list of integer l hanya mempunyai satu elemen
-- REALISASI
isOneElmt l = (length l) == 1 


-- =======================================================================

add :: Int -> [Int] -> [Int]
add x l 
    | isEmpty l = [x]
    | x <= head l = konso x l
    | otherwise = konso (head l) (add x (tail l))

sort :: [Int] -> [Int]
-- mengurutkan list of integer secara ascending
sort l
    | isEmpty l = []
    | otherwise = add (head l) (sort (tail l)) 

list1 :: [Int] -> [Int]
list1 l 
    | isOneElmt (tail l) = [head l]
    | isOneElmt l = [head l]
    | otherwise = 
        konso (head l) (list1 (tail (init l)))

list2 :: [Int] -> [Int]
list2 l
    | isOneElmt l = []
    | isOneElmt (init l) = [last l]
    | otherwise = 
        konsDot (list2 (tail (init l))) (last l)

merge :: [Int] -> [Int] -> [Int]
merge l1 l2
    | isEmpty l1 = l2
    | otherwise = konso (head l1) (merge (tail l1) l2)

alternateSort :: [Int] -> [Int]
alternateSort l =
    let
        sorted = sort l
        li1 = list1 sorted
        li2 = list2 sorted
        hasil = merge li1 li2
    in
        hasil

