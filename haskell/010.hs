import Primes (primes)
main = do
    print $ sum $ takeWhile (<10) primes
    print $ sum $ takeWhile (<1000000) primes
