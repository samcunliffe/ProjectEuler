
module Primes (primes, primesUpto) where

-- infinite list of primes using Eratosthenes sieve
primes = 2 : sieve [3,5..]
    where sieve (p:xs) = p : sieve [ x | x <- xs, x `mod` p /= 0 ]

primesUpto :: Integer -> [Integer]
primesUpto n = takeWhile (<n) primes

-- only sieves odd numbers with recursive sieve definition, filtering the further list by testing every element does not divide any element so far

