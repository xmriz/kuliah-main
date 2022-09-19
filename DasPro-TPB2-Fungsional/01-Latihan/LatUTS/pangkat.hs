-- PANGKAT              pangkat(a,b)

-- DEFINISI DAN SPESIFIKASI
pangkat :: Int -> Int -> Int
{- Fungsi pangkat menerima masukan berupa dua buah integer, a dan b, dan mengembalikan hasil berupa a^b (a pangkat b). 
Masukan diasumsikan selalu valid, yaitu a > 0 dan b ≥ 0. -}

-- REALISASI
pangkat a b
    | b == 0 = 1
    | otherwise = a * pangkat a (b-1)

-- APLIKASI
-- pangkat 3 2, hasilnya 9
-- pangkat 3 3, hasilnya 27