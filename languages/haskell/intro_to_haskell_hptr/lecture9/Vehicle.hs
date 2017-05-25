
module Vehicle where

data Propulsion = Wind
                | Diesel

data Vehicle = Ship { propulsion :: Propulsion, lengthFeet :: Double, passengerCap :: Int }
             | Car { maxSpeed :: Double, horsePower :: Double }
             | Plane { maxTravelHeight :: Double, maxVelocity :: Double }

price :: Vehicle -> Double
price (Ship propulsion lengthFeet passengerCap) = lengthFeet * 2.0
price (Car maxSpeed horsePower) = horsePower * 2.0
price (Plane maxTravelHeight maxVelocity) = maxTravelHeight * 10.0

