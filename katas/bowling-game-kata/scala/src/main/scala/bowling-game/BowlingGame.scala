package BowlingGame


class BowlingGame {
    var rolls: List[Int] = List()
    var frameIndex: Int = 0

    private def isSpare: Boolean = rolls(frameIndex) + rolls(frameIndex + 1) == 10

    private def frameScore: Int = {
        var sc = 0
        if (rolls(frameIndex) == 10) {
            sc += 10 + rolls(frameIndex + 1) + rolls(frameIndex + 2)
            frameIndex += 1
        } else if (isSpare) {
            sc += 10 + rolls(frameIndex + 2)
            frameIndex += 2
        } else {
            sc += rolls(frameIndex) + rolls(frameIndex + 1)
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
