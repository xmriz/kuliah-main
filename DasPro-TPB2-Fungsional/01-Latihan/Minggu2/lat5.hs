-- KONVERESI MATA UANG          convertUang(q,d,n,p)

-- DEFINISI DAN SPESIFIKASI
convertUang :: Int -> Int -> Int -> Int -> (Int, Int)
    {- convertUang(q,d,n,p) akan mengkonversi dari mata uang quarter (q), dime (d), nickel (n), dan penny (p) ke mata uang dollar dan sen -}

-- REALISASI
convertUang q d n p =
    let
        jumlahSen = (q*25) + (d*10) + (n*5) + (p*1)
    in
        ( div jumlahSen 100, mod jumlahSen 100 )

-- APLIKASI
-- convertUang 8 20 30 77