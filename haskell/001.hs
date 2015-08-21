main = print ( sum ( naturalMultiplesBelow 10 ), sum ( naturalMultiplesBelow 1000 ) )

-- all natural numbers below n that are multiples of 3 or 5
naturalMultiplesBelow :: (Integral a) => a -> [a]
naturalMultiplesBelow n = [ x | x <- [1..n-1], rem x 3 == 0 || rem x 5 == 0 ]
