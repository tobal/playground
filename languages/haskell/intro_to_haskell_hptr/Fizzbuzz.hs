
module Main where

fizzBuzz :: Integer -> String
fizzBuzz input = if input `mod` 3 == 0 then (if input `mod` 5 == 0 then "FizzBuzz" else "Fizz") else (if input `mod` 5 == 0 then "Buzz" else (show input))

main :: IO ()
main = putStrLn (fizzBuzz 14)

