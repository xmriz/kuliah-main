module HitungIndeks where

hitungIndeks :: Float -> Float -> Float -> Int 

hitungIndeks a b c
    | (a >= 75) && (b >= 75) && (c >= 75) = 4
    | (a == 0) || (b == 0) || (c == 0) = 0
    | (c < 40) && (a >= 40) && (b >= 40) = 2
    | (a < 40) || (b < 40) = 1
    | (a < 75) && (a >= 40) && (b < 75) && (b >= 40) && (c < 75) && (c >= 40) = 2
    | ((a >= 75) && (b >= 75)) || ((a >= 75) && (c >= 75)) || ((b >= 75) && (c >= 75)) = 3