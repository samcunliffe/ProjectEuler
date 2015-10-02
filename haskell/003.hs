import Primes (primesUpto)

main = do
    print(primeFactors 13195)
    print(head(primeFactors 600851475143))

primeFactors :: Integer -> [Integer]
primeFactors n = [ x | x <- rev_primes, n `mod` x == 0 ]
    where rev_primes = reverse $ primesUpto $ floor $ sqrt $ fromIntegral n
