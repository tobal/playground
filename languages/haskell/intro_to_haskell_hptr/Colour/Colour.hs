
module Colour where

data Colour = Red
            | Green
            | Blue
            | Yellow
            | Brown
            deriving (Show, Eq)

data Knight = Arthur
            | Galahad
            | Robin
            | Lancelot
            | Bedevere
            deriving (Show, Eq)

aColour :: Colour
aColour = Blue

someColours :: [Colour]
someColours = [Red, Green, Brown]

favouriteColour :: Knight -> Colour
favouriteColour knight
                | knight == Arthur = Red
                | knight == Galahad = Green
                | knight == Robin = Blue
                | knight == Lancelot = Yellow
                | knight == Bedevere = Brown

