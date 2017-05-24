
module Vehicle where

data Propulsion = Wind
                | Diesel

data Ship = S { propulsion :: Propulsion, lengthFeet :: Double, passengerCap :: Int }

data Car = C { maxSpeed :: Double, horsePower :: Double }

data Plane = P { maxTravelHeight :: Double, maxVelocity :: Double }

data Vehicle = Ship
             | Car
             | Plane

