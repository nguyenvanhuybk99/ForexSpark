import fetcher.{Fetcher, KafkaFetcher}
import fetcher.info.{HDFSInfo, KafkaInfo}

object Main extends App{

  val defaultFS = "hdfs://hadoop-namenode:8020"

//  val sourceInfo1 = new KafkaInfo("TASK-EVENT")
//  val sinkInfo1 = new HDFSInfo("/data/task-event", "task_event", defaultFS)
//  val fetcher1 = new KafkaFetcher(sourceInfo1, sinkInfo1)
//
//  val sourceInfo2 = new KafkaInfo("TASK-USAGE")
//  val sinkInfo2 = new HDFSInfo("/data/task-usage", "task_event", defaultFS)
//  val fetcher2 = new KafkaFetcher(sourceInfo2, sinkInfo2)

  val sourceInfo1 = new KafkaInfo("USDEUR")
  val sinkInfo1 = new HDFSInfo("/data/task-usdeur", "task_usdeur", defaultFS)
  val fetcher1 = new KafkaFetcher(sourceInfo1, sinkInfo1)

  val sourceInfo2 = new KafkaInfo("GBPUSD")
  val sinkInfo2 = new HDFSInfo("/data/task-gbpusd", "task_gbpusd", defaultFS)
  val fetcher2 = new KafkaFetcher(sourceInfo2, sinkInfo2)

  val manager = new LogBatchManager(List[Fetcher](fetcher1, fetcher2))
  try {
    manager.run
  } catch {
    case _: Throwable => manager.stop
  }
}
