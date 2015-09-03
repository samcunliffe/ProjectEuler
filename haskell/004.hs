import Data.List (find)

main = print ( maximum palindromes2, maximum palindromes3 )

reverse' :: Integer -> Integer
reverse' n = read ( reverse ( show n ) ) :: Integer

isPalindrome :: Integer -> Bool
isPalindrome n = reverse' n == n

threeDigitNumbers = [999,998..100]
twoDigitNumbers = [99,98..10]

products li = [ x*y | x <- li, y <- li, x <= y ]
palindromes2 = [ x | x <- products twoDigitNumbers, isPalindrome x]
palindromes3 = [ x | x <- products threeDigitNumbers, isPalindrome x]


