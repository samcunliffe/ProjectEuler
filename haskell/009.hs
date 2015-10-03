main = print $ (\ (a,b,c) -> a*b*c) $ getSumEq 1000 triples

-- Euclid's formula
--   https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
euclid :: Int -> Int -> (Int, Int, Int)
euclid m n = (a, b, c)
    where a = (m*m - n*n)
          b = 2*m*n
          c = (m*m + n*n)

-- list of all reasonable triples ( must be less than (sqrt(1000))**2 + 0*0 )
triples = [ euclid m n | m <- [2..32], n <- [1..(m-1)] ]

-- find the triple whose sum equals n
getSumEq :: Int -> [(Int, Int, Int)] -> (Int, Int, Int)
getSumEq n [] = (0,0,0)
getSumEq n (x:xs)
    | a+b+c == n  = x
    | otherwise   = getSumEq n xs
    where (a,b,c) = x
