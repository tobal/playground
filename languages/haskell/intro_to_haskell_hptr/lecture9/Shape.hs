
module Shape where

data Shape = Triangle {a :: Double, b :: Double, c :: Double}
           | Rectangle {width :: Double, height :: Double}

perimeter :: Shape -> Double
perimeter (Triangle a b c) = a + b + c
perimeter (Rectangle width height) = 2 * (width + height)

report :: Shape -> String
report shape = let perimeter = case shape of
                                    (Triangle a b c) -> a + b + c
                                    (Rectangle width height) -> 2 * (width + height)
               in "perimeter of shape: " ++ show perimeter
