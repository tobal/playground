package BowlingGame


class BowlingGame {
    var rolls: List[Int] = List()
    var frameIndex: Int = 0

    private def isSpare: Boolean = rolls(frameIndex) + rolls(frameIndex + 1) == 10

    private def isStrike: Boolean = rolls(frameIndex) == 10

    private def sumOfBallsInFrame: Int = rolls(frameIndex) + rolls(frameIndex + 1)

    private def spareBonus: Int = rolls(frameIndex + 2)

    private def strikeBonus: Int = rolls(frameIndex + 1) + rolls(frameIndex + 2)

    private def frameScore: Int = {
        var sc = 0
        if (isStrike) {
            sc += 10 + strikeBonus
            frameIndex += 1
        } else if (isSpare) {
            sc += 10 + spareBonus
            frameIndex += 2
        } else {
            sc += sumOfBallsInFrame
            frameIndex += 2
        }
        sc
    }

    def roll(pins: Int): Any = {
        rolls = rolls :+ pins
    }

    def score: Int = {
        var sc = 0
        frameIndex = 0
        for {
            frame <- 0 until 10
        } yield sc += frameScore
        sc
    }
}
