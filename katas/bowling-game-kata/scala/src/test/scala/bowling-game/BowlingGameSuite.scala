import org.scalatest.FunSpec
import org.scalatest.matchers.ShouldMatchers
import org.scalatest.BeforeAndAfterEach

import BowlingGame._

class BowlingGameTest extends FunSpec with ShouldMatchers with BeforeAndAfterEach{
    private var g: BowlingGame = new BowlingGame

    private def rollMany(n: Int, pins: Int) {
        for {
            i <- 0 until n
        } yield g.roll(pins)
    }

    override def beforeEach() {
        g = new BowlingGame
    }

    describe("BowlingGame") {
        it ("scores zero on gutter game") {
            rollMany(20, 0)
            g.score should equal (0)
        }

        it ("scores 20 on all ones game") {
            rollMany(20, 1)
            g.score should equal (20)
        }

//        it ("takes one spare into account") {
//            g.roll(5)
//            g.roll(5)
//            g.roll(3)
//            rollMany(17, 0)
//            g.score should equal (16)
//        }
    }
}
