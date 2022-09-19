-- MeanOlympique            mo(a,b,c,d)

-- DEFINISI DAN SPESIFIKASI
mo :: Float -> Float -> Float -> Float -> Float
    {-mo(a,b,c,d) menghasilkan nilai rata-rata dari
    dua dia antara a, b, c, d dengan mengabaikan nilai
    terbesar dan terkecil-}

-- REALISASI
-- versi tanpa abstraksi
mo a b c d =
    let -- fungsi lokal, tidak bisa digunakan diluar lingkup
        maxab = (a+b + abs(a-b))/2
        maxcd = (c+d + abs(c-d))/2
        minab = (a+b - abs(a-b))/2
        mincd = (c+d - abs(c-d))/2
    in
        let
            max = (maxab+maxcd + abs(maxab-maxcd))/2
            min = (minab+mincd - abs(minab-mincd))/2
        in
            (a+b+c+d-max-min)/2
            