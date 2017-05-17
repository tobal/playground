
module Main where

cylinderVolume :: Double -> Double -> Double
cylinderVolume radius height = let square x = x * x
                                   baseArea = (square radius) * pi
                                in baseArea * height

computePi :: Double
computePi = cylinderVolume 1.0 1.0

main :: IO ()
main = print computePi

