# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from log_manager import LogManager
from connector import KafkaConnector
from config import LoggerConfig, ConnectorConfig

import sys


class Main:
    __log_manager: LogManager

    @classmethod
    def setup(cls, msg_num=1, rate=1):
        task_usdeur_logger_config = LoggerConfig("TASK_USDEUR", 2)
        task_usdeur_connector_config = ConnectorConfig("KAFKA_CONNECTOR", "USDEUR")
        task_gbpusd_logger_config = LoggerConfig("TASK_GBPUSD", 2)
        task_gbpusd_connector_config = ConnectorConfig("KAFKA_CONNECTOR", "GBPUSD")

        cls.__log_manager = LogManager([(task_usdeur_logger_config, task_usdeur_connector_config),
                                        (task_gbpusd_logger_config, task_gbpusd_connector_config)],
                                       msg_num, rate)

        return cls

    @classmethod
    def run(cls):
        cls.__log_manager.dispatch_logs()


if __name__ == '__main__':
    args = sys.argv
    try:
        app = Main.setup(int(args[1]), int(args[2]))
    except Exception as e:
        print(e)
        print("Wrong arguments, use default config")
        app = Main.setup(3, 4)
    app.run()
