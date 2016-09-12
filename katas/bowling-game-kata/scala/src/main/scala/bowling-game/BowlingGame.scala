package BowlingGame


class BowlingGame {
    var rolls: List[Int] = List()

    private def frameScore(frameIndex: Int): Int = {
        var sc = 0
        val idx = frameIndex * 2
        if (rolls(idx) + rolls(idx + 1) == 10)
            sc += 10 + rolls(idx + 2)
        else
            sc += rolls(idx) + rolls(idx + 1)
        sc
    }

    def roll(pins: Int): Any = {
        rolls = rolls :+ pins
    }

    def score: Int = {
        var sc = 0
        for {
            i <- 0 until 10
        } yield sc += frameScore(i)
        sc
    }
}
