package com.sap1ens.workshop

import akka.actor.{Actor, ActorRef, ActorSystem, Props}

object JobQueueApplication extends App {
  import SimpleActor._

  val system = ActorSystem("MySystem")
  val greeter = system.actorOf(Props[SimpleActor], name = "simpleWorker")
  greeter ! SimpleMessage("Csojj")
}
