
module Ship where

data Propulsion = Wind
                | Diesel

data Ship = S { propulsion :: Propulsion, lengthFeet :: Double, passengerCap :: Int }
