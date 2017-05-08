
module Main where

concatenate :: String -> String -> String
concatenate in1 in2 = in1 ++ in2

greets :: String -> String -> String
greets who whom = concatenate (concatenate who ": Hello ") whom

main :: IO ()
main = putStrLn ("Luke" `greets` "Leia")

