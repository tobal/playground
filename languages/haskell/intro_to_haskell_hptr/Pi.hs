
module Main where

cylinderVolume :: Double -> Double -> Double
cylinderVolume radius height = baseArea * height
    where square x = x * x
          baseArea = (square radius) * pi

computePi :: Double
computePi = cylinderVolume 1.0 1.0

main :: IO ()
main = print computePi

