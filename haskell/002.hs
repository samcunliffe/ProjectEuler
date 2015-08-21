main = print ( sum [ fn | fn <- fibonacciLessThan 4000000, isEven fn ])

-- fibonacci sequence implemented as the mathsy definition
fibonacci :: Integer -> Integer
fibonacci 0 = 1
fibonacci 1 = 1
fibonacci n = fibonacci(n-1) + fibonacci(n-2)

-- check a number is even
isEven :: Integer -> Bool
isEven n = rem n 2 == 0

-- infinite sequence of fibonnaci numbers
infiniteFibonacci = [fibonacci n | n <- [1..]]

-- fibonacci less than 4million
fibonacciLessThan :: Integer -> [Integer]
fibonacciLessThan n = takeWhile (<n) infiniteFibonacci
