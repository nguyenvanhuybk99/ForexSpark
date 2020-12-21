# author: Huy.Nguyen
# institute: Hanoi University of Science and Technology
# file name: _task_event_logger.py
# project name: LogProducer
# date: 25/11/2020

from logger._logger import Logger
from logger._record import TaskGbpUsdRecord
from iostream import TaskGbpUsdLoader
from config import LoggerConfig


class TaskGbpUsdLogger(Logger):

    __instance__ = None

    def __init__(self, config: LoggerConfig):
        if TaskGbpUsdLogger.__instance__ is None:
            super().__init__()
            self.__config = config
            self._loader = TaskGbpUsdLoader()
            self._recorder = TaskGbpUsdRecord()
            TaskGbpUsdLogger.__instance__ = self
        else:
            raise Exception("Cannot create another instance of {}".format(self.__class__))

    @classmethod
    def get_instance(cls, config: LoggerConfig):
        if cls.__instance__ is None:
            TaskGbpUsdLogger(config)
        return cls.__instance__

    def get_name(self):
        return "GBPUSD LOGGER"
