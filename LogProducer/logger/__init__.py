# author: Huy.Nguyen
# institute: Hanoi University of Science and Technology
# file name: __init__.py
# project name: LogProducer
# date: 15/12/2020

from logger._logger import Logger
from logger._task_gbpusd_logger import TaskGbpUsdLogger
from logger._task_usdeur_logger import TaskUsdEurLogger

__all__ = [
    'Logger',
    'TaskGbpUsdLogger',
    'TaskUsdEurLogger'
]
