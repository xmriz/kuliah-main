lambda1 = (\x -> x**2) 4 --16

lambda2 = (\(x,y) -> x+y) (2,3) --5

lambda3 = (\x -> (\y -> x+y) 3) 2 --5