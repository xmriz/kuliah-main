-- JUMLAH BILANNGAN             sumRange(a,b)

-- DEFINISI DAN SPESIFIKASI
sumRange :: Int -> Int -> Int 
    {- sumRange(a,b) fungsi yang menerima masukan 2 bilangan integer (a dan b), dan menghasilkan penjumlahan semua bilangan a s.d. b,
    dengan syarat a <= b, dan keduanya bilangan positif -}

-- REALISASI
sumRange a b 
    | a == b = a --basis
    | otherwise = sumRange a (b-1) + b --rekurens

-- APLIKASI 
-- sumRange 2 4