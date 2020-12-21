from pyspark.sql import SparkSession
from trainers.task_usdeur_trainer import TaskUsdEurTrainer


class Main():

    def __init__(self, master, app_name, model_path, memory="1024m"):
        self.spark_session = SparkSession.builder \
            .master(master) \
            .appName(app_name) \
            .config("spark.executor.memory", memory) \
            .config("spark.executor.core", "1") \
            .getOrCreate()
        self.task_trainer = TaskUsdEurTrainer(model_path, spark_session=self.spark_session)

    def run(self):
        self.task_trainer.train()


if __name__ == "__main__":

    app = Main("spark://spark-master:7077", "Trainer","hdfs://hadoop-namenode:8020/data/model/task-usdeur", "1024m")
    app.run()