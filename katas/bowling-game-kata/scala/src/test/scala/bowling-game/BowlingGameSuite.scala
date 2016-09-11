import org.scalatest.FunSpec
import org.scalatest.matchers.ShouldMatchers

import BowlingGame._

class BowlingGameTest extends FunSpec with ShouldMatchers {
    describe("BowlingGame") {
        it ("scores zero on gutter game") {
            val g: BowlingGame = new BowlingGame
            for {
                i <- 0 until 20
            } yield g.roll(0)
            g.score should equal (0)
        }

        it ("scores 20 on all ones game") {
            val g: BowlingGame = new BowlingGame
            for {
                i <- 0 until 20
            } yield g.roll(1)
            g.score should equal (20)
        }
    }
}
