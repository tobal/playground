implicit val actorSystem = ActorSystem("akka-streams-example")
implicit val materializer = ActorMaterializer()
val helloWorldStream: RunnableGraph[NotUsed] =
  Source.single("Hello world")
    .via(Flow[String].map(s => s.toUpperCase()))
    .to(Sink.foreach(println))
helloWorldStream.run()
