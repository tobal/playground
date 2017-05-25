
module Vehicle where

data Propulsion = Wind
                | Diesel

data Vehicle = Ship { propulsion :: Propulsion, lengthFeet :: Double, passengerCap :: Int }
             | Car { maxSpeed :: Double, horsePower :: Double }
             | Plane { maxTravelHeight :: Double, maxVelocity :: Double }

price :: Vehicle -> Double
price vehicle = case vehicle of
                     (Ship propulsion lengthFeet passengerCap) = lengthFeet * 2.0
                     (Car maxSpeed horsePower) = horsePower * 2.0
                     (Plane maxTravelHeight maxVelocity) = maxTravelHeight * 10.0

