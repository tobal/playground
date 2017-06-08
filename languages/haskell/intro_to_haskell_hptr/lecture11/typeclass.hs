
concatString :: (Show a, Show b) => a -> b -> String
concatString x y = show x ++ show y

class Typeclass a where
    methodToImplement :: a -> String

data Propulsion = Wind | Diesel deriving (Show, Ord)

--data Propulsion = Wind | Diesel
--
--instance Show Propulsion where
--    show Wind = "Wind"
--    show Diesel = "Diesel"

instance Eq Propulsion where
    (==) Wind Wind = True
    (==) Diesel Diesel = True
    (==) Wind Diesel = False
    (==) Diesel Wind = False

plusTwo :: (Num a) => a -> a
plusTwo x = x + 2
