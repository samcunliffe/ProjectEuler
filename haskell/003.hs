import Primes (primesUpto)

main = do
    print(primeFactors 13195)
    print(last(primeFactors 600851475143))

primeFactors :: Integer -> [Integer]
primeFactors n = [ x | x <- relavent_primes, n `mod` x == 0 ]
    where relavent_primes = primesUpto $ floor $ sqrt $ fromIntegral n
