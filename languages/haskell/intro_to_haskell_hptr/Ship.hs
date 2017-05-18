
module Ship where

data Propulsion = Wind
                | Diesel

data Ship = S Propulsion Double Int
