
module Primes (primes, primesUpto, primeFactors) where

-- infinite list of primes using Eratosthenes sieve
primes = 2 : sieve [3,5..]
    where sieve (p:xs) = p : sieve [ x | x <- xs, x `mod` p /= 0 ]

primesUpto :: Integer -> [Integer]
primesUpto n = takeWhile (<n) primes

-- only sieves odd numbers with recursive sieve definition, filtering the further list by testing every element does not divide any element so far

-- this way is slow - first attempt
primeFactors' :: Integer -> [Integer]
primeFactors' n = [ x | x <- relavent_primes, n `mod` x == 0 ]
    where relavent_primes = primesUpto $ floor $ sqrt $ fromIntegral n

-- this way is taken from haskell wiki
--    https://wiki.haskell.org/Euler_problems/1_to_10#Problem_3 
--
-- recursive definition of factors which divides the number by it's prime factor each time
primeFactors :: Integer -> [Integer]
primeFactors n = factors n primes
    where
        factors n (p:ps)
            | p*p > n        = [n]                            -- termination condition
            | n `mod` p == 0 = p : factors (n `div` p) (p:ps) -- if we find a factor 
            | otherwise      = factors n ps                   -- if we don't 
