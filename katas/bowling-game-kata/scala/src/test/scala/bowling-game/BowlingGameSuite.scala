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

        }
    }
}
