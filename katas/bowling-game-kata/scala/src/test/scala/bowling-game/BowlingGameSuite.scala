import org.scalatest.FunSpec
import org.scalatest.matchers.ShouldMatchers

import BowlingGame._

class BowlingGameTest extends FunSpec with ShouldMatchers {
   describe("BowlingGame") {
       it ("answer") {
         BowlingGame.answer should equal (42)
       }
   }
}
