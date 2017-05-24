
module Shape where

data Shape = Triangle {a :: Double, b :: Double, c :: Double}
           | Rectangle {width :: Double, height :: Double}
