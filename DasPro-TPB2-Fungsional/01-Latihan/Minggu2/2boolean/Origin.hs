-- ORIGIN           isOrigin(x,y)

-- DEFINISI DAN SPESIFIKASI
isOrigin :: Int -> Int -> Bool
    {-isOrigin x y benar jika x dan y adalah nilai yang mewakili titik origin (0,0)-}

-- REALISASI
isOrigin x y =
    x == 0 && y == 0

-- APLIKASI
-- isOrigin 0 0