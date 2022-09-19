module SumKelipatanX where

sumKelipatanX :: Int -> Int -> Int -> Int 

sumKelipatanX m n x
    | m > n = 0
    | mod m x == 0 = m + sumKelipatanX (m+1) n x
    | otherwise = sumKelipatanX (m+1) n x