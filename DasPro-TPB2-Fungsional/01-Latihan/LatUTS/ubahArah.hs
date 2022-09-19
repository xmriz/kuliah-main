ubahArah :: Int -> Int -> Int 
    {- ubahArah s r adalah fungsi yang mereima masukan dua buah integer s dan r yang mempresentasikan arah pergerakan dan besar perubahan arah yang akan dilakukan (dalam satu derajat). Fungsi mengembalikan arah pergerakan yang baru dalam range 0 s.d. 359, setelah s diputar sebesar r. -}


-- REALISASI
ubahArah s r = 
    let 
        arah = s + r
    in 
        if arah > 359 then arah - 360
        else if arah < 0 then arah + 360
        else arah

-- APLIKASI
-- ubahArah 358 (-359), hasil : 359
-- ubahArah 350 100 , hasil : 90