
module Main where

averageCircleSpeed :: Double -> [Double] -> Double
averageCircleSpeed radius laps = let circumference r = 2 * r * pi
                                     someStuff l = fromIntegral (length l)
                                  in (circumference radius) / ((sum laps) / (someStuff laps))

compute :: Double
compute = averageCircleSpeed 1.0 [2.1, 2.2]

main :: IO ()
main = print compute

