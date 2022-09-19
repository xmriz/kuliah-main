-- DEFINISI DAN SPESIFIKASI LIST
{- type List of Float: [ ] atau [e o List] atau [List o e]  
   Definisi type List of Float
   Basis: List of Float kosong adalah list of Float 
   Rekurens: 
   List tidak kosong dibuat dengan menambahkan sebuah elemen bertype Float di awal 
   sebuah list atau
   dibuat dengan menambahkan sebuah elemen bertype Float di akhir sebuah list -}

-- DEFINISI DAN SPESIFIKASI KONSTRUKTOR
konso :: Float -> [Float] -> [Float]
{- konso e li menghasilkan sebuah list of Floateger dari e (sebuah Floateger) dan li 
   (list of Floateger), dengan e sebagai elemen pertama: e o li -> li' -}
-- REALISASI
konso e li = [e] ++ li

konsDot :: [Float] -> Float -> [Float]
{- konsDot li e menghasilkan sebuah list of Floateger dari li (list of Floateger) dan 
   e (sebuah Floateger), dengan e sebagai elemen terakhir: li o e -> li' -}
-- REALISASI
konsDot li e = li ++ [e]

-- DEFINISI DAN SPESIFIKASI SELEKTOR
-- head :: [Float] -> Float
-- head l menghasilkan elemen pertama list l, l tidak kosong

-- tail :: [Float] -> [Float]
-- tail l menghasilkan list tanpa elemen pertama list l, l tidak kosong

-- last :: [Float] -> Float
-- last l menghasilkan elemen terakhir list l, l tidak kosong

-- init :: [Float] -> [Float]
-- init l menghasilkan list tanpa elemen terakhir list l, l tidak kosong

-- DEFINISI DAN SPESIFIKASI PREDIKAT
isEmpty :: [Float] -> Bool
-- isEmpty l  true jika list of Floateger l kosong
-- REALISASI
isEmpty l = null l

isOneElmt :: [Float] -> Bool
-- isOneElmt l true jika list of Floateger l hanya mempunyai satu elemen
-- REALISASI
isOneElmt l = (length l) == 1 

-- ===================================================================================

-- OffsetList

-- DEFINISI DAN SPESIFIKASI
offsetList :: (Float -> Float) -> (Float -> Float) -> Float -> Float -> [Float]
    {-Fungsi offsetList menerima masukan dua buah fungsi, misalnya f dan g, serta dua buah bilangan riil (float), a dan b. 
    Fungsi offsetList akan menghasilkan sebuah list of float yang merupakan penerapan fungsi f terhadap 
    bilangan float antara a dan b, dimulai dari a dengan increment menggunakan fungsi g.-}

-- REALISASI
offsetList f g a b
    | a > b = []
    | otherwise = konso (f a) (offsetList f g (g a) b)

-- APLIKASI
-- offsetList (\x -> x) (\x -> x+2) 1.2 7.1 ; hasil : [1.2,3.2,5.2]
-- offsetList (\x -> if x<0 then (-999) else (x+3.2)) (\x -> x+0.5) (-1.0) 1.0 ; hasil : [-999.0,-999.0,3.2,3.7,4.2]


-- offsetList (\x -> x*x) (\x -> x+1) 0.0 9.0