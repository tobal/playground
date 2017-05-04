


object Excercise1 {
  def main(args: Array[String]): Unit = {
    val lines = scala.io.Source.fromFile("team.csv").getLines
    val data = for (
         line <- lines
    ) yield (line.split(",").toList)

    val g = for (team <- data
    ) yield (team(0), team(1))
    println("Most goals")
    g.toList.sortWith(_._2 < _._2) foreach println
  }
}

