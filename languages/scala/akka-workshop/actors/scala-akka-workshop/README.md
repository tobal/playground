# Scala/Akka Workshop

## Job Queue Exercise
 
Let's build a [job queue](https://en.wikipedia.org/wiki/Job_queue)! 
 
In our case we're going to have `JobExecutor` actor that accepts incoming job requests and executes them using pool of `JobWorker` actors. If one of the `JobWorker` actors fails `JobExecutor` should restart failed job. Also `JobWorker`s should communicate results to `JobExecutor`.

A job itself can be anything (read or write a file, calculate something, etc.), but I suggest to download a file from specified URL and save it to local disk with provided path. Ideally we should introduce a percent of failures, so we can see restarts as well.

A few important things: 

- All Akka dependencies are already included in build.sbt
- You can run the application with `sbt run`
- Check `SimpleActor` and `Helpers` files
- Use case classes to represent jobs
- You will probably need to use routing
