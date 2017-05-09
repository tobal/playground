
module Main where

fizzBuzz :: Integer -> String
fizzBuzz input
    | input `mod` 15 == 0 = "FizzBuzz"
    | input `mod` 3 == 0 = "Fizz"
    | input `mod` 5 == 0 = "Buzz"
    | otherwise = show input

main :: IO ()
main = putStrLn (fizzBuzz 9)

