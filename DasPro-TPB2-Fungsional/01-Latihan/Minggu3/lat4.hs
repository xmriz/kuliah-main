-- JUMLAH DIGIT         sumOfDigitsPosNeg(x)

-- DEFINISI DAN SPESIFIKASI
sumOfDigitsPosNeg :: Int -> Int 
    {- sumOfDigitsPosNeg(x) menghitung hasil penjumlahan dari setiap bilangan tunggal yang terdapat di dalam sebuah bilangan integer positif. 
    Apabila x bilangan negatif, maka tanda negatif di abaikan. -}

-- REALISASI
sumOfDigitsPosNeg x 
    | x >= 0 =
        if x == 0 then 0 --basis
        else (mod x 10) + (sumOfDigitsPosNeg (div x 10)) --rekurens
    | otherwise = 
        sumOfDigitsPosNeg (-x)

-- APLIKASI
-- sumOfDigitsPosNeg 345
-- sumOfDigitsPosNeg (-345)