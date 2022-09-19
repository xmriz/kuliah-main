tes :: Int -> Int 

tes n
    | n == 0 = 0
    | otherwise = tes (n-1) + (5*n -4)