package BowlingGame


class BowlingGame {
    var currentScore: Int = 0

    def roll(pins: Int): Any = {
        currentScore += pins
    }

    def score: Int = currentScore
}
