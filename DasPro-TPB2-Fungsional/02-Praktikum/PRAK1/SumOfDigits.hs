module SumOfDigits where

sumOfDigits :: Int -> Int
-- sumOfDigits n menghasilkan penjumlahan setiap bilangan tunggal yang membentuk n
-- prekondisi n >= 0

sumOfDigits x
    | x >= 0 =
        if x == 0 then 0 --basis
        else (mod x 10) + (sumOfDigits (div x 10))
        