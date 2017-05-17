
module Main where

averageCircleSpeed :: Double -> [Double] -> Double
averageCircleSpeed radius laps =(circumference radius) / ((sum laps) / (someStuff laps)) 
    where circumference r = 2 * r * pi
          someStuff l = fromIntegral (length l)

compute :: Double
compute = averageCircleSpeed 1.0 [2.1, 2.2]

main :: IO ()
main = print compute

