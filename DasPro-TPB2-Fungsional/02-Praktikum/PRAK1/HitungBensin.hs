module HitungBensin where

hitungBensin :: Int -> Int -> Int 

hitungBensin a b
    | a == b = 0
    | otherwise =
        if mod a 2 == 0 then
            hitungBensin (div a 2) b + 1
        else 
            hitungBensin ((3*a)+1) b + 1