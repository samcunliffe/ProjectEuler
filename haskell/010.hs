import Primes (primes)
import System.TimeIt (timeIt)
main = do
    print $ sum $ takeWhile (<10) primes
    timeIt $ print $ sum $ takeWhile (<2000000) primes
