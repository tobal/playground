
module Ship where

data Propulsion = Wind
                | Diesel

data Ship = S Propulsion Double Int

propulsion :: Ship -> Propulsion
propulsion (S propulsion lengthFeet passengerCap) = propulsion

lengthFeet :: Ship -> Double
lengthFeet (S propulsion lengthFeet passengerCap) = lengthFeet

passengerCap :: Ship -> Int
passengerCap (S propulsion lengthFeet passengerCap) = passengerCap
