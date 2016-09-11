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

    describe("BowlingGame") {
        it ("scores zero on gutter game") {
            for {
                i <- 0 until 20
            } yield g.roll(0)
            g.score should equal (0)
        }

        it ("scores 20 on all ones game") {
            for {
                i <- 0 until 20
            } yield g.roll(1)
            g.score should equal (20)
        }
    }
}
