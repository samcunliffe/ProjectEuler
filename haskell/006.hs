main = do
    let sumSqFirstTen = sumSq [1..10] 
    let sqSumFirstTen = ( sum [1..10] )**2 
    print ((sumSqFirstTen, sqSumFirstTen, sqSumFirstTen-sumSqFirstTen))

    let sumSqFirstHundred = sumSq [1..100] 
    let sqSumFirstHundred = ( sum [1..100] )**2 
    print ((sumSqFirstHundred, sqSumFirstHundred, sqSumFirstHundred-sumSqFirstHundred))

sumSq :: (Num a) => [a] -> a
sumSq li = foldl (\ acc x -> acc + x*x) 0 li
