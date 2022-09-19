-- KONVERSI WAKTU               hhmmdd(x)

-- DEFINISI DAN SPESIFIKASI
hhmmdd :: Int -> (Int, Int, Int, Int)

hhmmdd x = ( div x 86400, div (mod x 86400) 3600, div (mod (mod x 86400) 3600) 60, mod (mod (mod x 86400) 3600) 60 )