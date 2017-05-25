
module Shape where

data Shape = Triangle {a :: Double, b :: Double, c :: Double}
           | Rectangle {width :: Double, height :: Double}

perimeter :: Shape -> Double
perimeter (Triangle a b c) = a + b + c
perimeter (Rectangle width height) = 2 * (width + height)
