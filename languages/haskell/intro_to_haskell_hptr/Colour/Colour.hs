
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
favouriteColour Arthur = Red
favouriteColour Galahad = Green
favouriteColour Robin = Blue
favouriteColour Lancelot = Yellow
favouriteColour Bedevere = Brown

