-- APAKAH DATE VALID?            isDateValid(d,m,y)

-- DEFINISI DAN SPESIFIKASI
isDateValid :: Int -> Int -> Int -> Bool
    {- isDateValid(d,m,y) mengembalikan nilai true jika d, m, y membentuk date yang valid.
    Definisi date yang valid adalah jika elemen dari (d) bernilai antara 1 dan 31, tergantung
    pada bulan dan apakah tahun kabisat atau bukan, elemen bulan (m) bernilai antara 1 dan 12,
    dan elemen tahun (y) bernilai antara 0 dan 99. Nilai y mewakili tahun 1900 s.d. 1999 -}

-- REALISASI
isDateValid d m y
    | ((mod (y+1900) 4 == 0) && (mod (y+1900) 100 /= 0)) || (mod (y+1900) 400 == 0) = -- kabisat
        if (m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12) then --bulan berhari 31
            if (y >= 0 && y <= 99) && (m >= 1 && m <= 12) && (d >= 1 && d <= 31) then True
            else False  
        else if (m == 4 || m == 6 || m == 9 || m == 11) then --bulan berhari 30
            if (y >= 0 && y <= 99) && (m >= 1 && m <= 12) && (d >= 1 && d <= 30) then True
            else False 
        else if m == 2 then --bulan februari
            if (y >= 0 && y <= 99) && (m >= 1 && m <= 12) && (d >= 1 && d <= 29) then True
            else False 
        else False
    | otherwise =
        if (m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12) then 
            if (y >= 0 && y <= 99) && (m >= 1 && m <= 12) && (d >= 1 && d <= 31) then True
            else False  
        else if (m == 4 || m == 6 || m == 9 || m == 11) then
            if (y >= 0 && y <= 99) && (m >= 1 && m <= 12) && (d >= 1 && d <= 30) then True
            else False 
        else if m == 2 then
            if (y >= 0 && y <= 99) && (m >= 1 && m <= 12) && (d >= 1 && d <= 28) then True
            else False 
        else False

