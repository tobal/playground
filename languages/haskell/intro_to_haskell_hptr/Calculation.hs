
module Main where

double :: Int -> Int
double n = n * 2

times :: Int -> Int -> Int
times n multiplier = n * multiplier

calculation :: Int
calculation = times (double 10) 20

main :: IO ()
main = print calculation
