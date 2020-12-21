# author: Khanh.Quang
# institute: Hanoi University of Science and Technology
# file name: _task_event_logger.py
# project name: LogProducer
# date: 25/11/2020

from logger._logger import Logger
from logger._record import TaskUsdEurRecord
from iostream import TaskUsdEurLoader
from config import LoggerConfig


class TaskUsdEurLogger(Logger):

    __instance__ = None

    def __init__(self, config: LoggerConfig):
        if TaskUsdEurLogger.__instance__ is None:
            super().__init__()
            self.__config = config
            self._loader = TaskUsdEurLoader()
            self._recorder = TaskUsdEurRecord()
            TaskUsdEurLogger.__instance__ = self
        else:
            raise Exception("Cannot create another instance of {}".format(self.__class__))

    @classmethod
    def get_instance(cls, config: LoggerConfig):
        if cls.__instance__ is None:
            TaskUsdEurLogger(config)
        return cls.__instance__

    def get_name(self):
        return "USDEUR LOGGER"
