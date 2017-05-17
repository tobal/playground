
module Main where

averageCircleSpeed :: Double -> [Double] -> Double
averageCircleSpeed radius laps = 2 * radius * pi / ((sum laps) / (fromIntegral (length laps)))

compute :: Double
compute = averageCircleSpeed 1.0 [2.1, 2.2]

main :: IO ()
main = print compute

