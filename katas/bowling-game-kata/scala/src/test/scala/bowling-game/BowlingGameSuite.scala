import org.scalatest.FunSpec
import org.scalatest.matchers.ShouldMatchers
import org.scalatest.BeforeAndAfterAllConfigMap
import org.scalatest.ConfigMap

import BowlingGame._

class BowlingGameTest extends FunSpec with ShouldMatchers with BeforeAndAfterAllConfigMap {
    private var g: BowlingGame = new BowlingGame

    override def beforeAll(configMap: ConfigMap) {
        g = new BowlingGame
    }

    private def rollMany(n: Int, pins: Int) {
        for {
            i <- 0 until n
        } yield g.roll(pins)
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
    }
}
