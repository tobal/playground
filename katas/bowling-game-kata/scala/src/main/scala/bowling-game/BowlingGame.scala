package BowlingGame


class BowlingGame {
    var rolls: List[Int] = List()

    def roll(pins: Int): Any = {
        rolls = rolls :+ pins
    }

    def score: Int = {
        rolls.foldLeft(0)(_ + _)
    }
}
