module JamLembur where

jamLembur :: Int -> Int -> Int -> (Bool, Int, Int, Int)

jamLembur j m d =
    let 
        jamLembur = (16*3600) + (20*60)
        jamResmi = (16*3600) + (30*60)
        jamPulang = (j*3600) + (m*60) + d
        selisih = abs(jamPulang - jamResmi)
    in
        if jamPulang <= jamLembur then
            (False , div selisih 3600, div (mod selisih 3600) 60, mod (mod selisih 3600) 60)
        else
            (True , div selisih 3600, div (mod selisih 3600) 60, mod (mod selisih 3600) 60)