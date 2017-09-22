
module Main where

intMean :: Integral a => [a] -> Maybe a
intMean [] = Nothing
intMean nums = let sumOfNums = sum nums
                   len = fromIntegral (length nums)
               in Just (sumOfNums `div` len)

main :: IO ()
main = print (intMean [1, 2, 3])
