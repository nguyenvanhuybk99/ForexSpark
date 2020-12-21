# author: Khanh.Quang
# institute: Hanoi University of Science and Technology
# file name: _task_usage_loader.py
# project name: LogProducer
# date: 25/11/2020

from iostream._loader import Loader

import re


class TaskUsdEurLoader(Loader):
    __source = "data/usdeur/usdeur_1027_1210.csv"

    def __init__(self):
        self.__file = open(self.__source)

    def _connection(self):
        return self.__file

    def _get_event_time(self, line: str) -> float:
        result = re.match("([0-9]*),([0-9]*)-(.*)", line)
        if result is None:
            return -1
        else:
            return int(result.group(1))
