-- PANGKAT3         fx3(x)

-- DEFINISI DAN SPESIFIKASI
fx2 :: Int -> Int
    {-fx2(x) menghitung pangkat dua dari x, x sebuah bilangan integer-}
fx3 :: Int -> Int
    -- fx3(x) menghitung pangkat tiga dari x, sebuah bilangan integer

-- REALISASI
fx3 x = (fx2 x)*x
fx2 x = x*x

-- APLIKASI
-- fx3 2