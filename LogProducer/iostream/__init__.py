# author: Huy.Nguyen
# institute: Hanoi University of Science and Technology
# file name: __init__.py
# project name: LogProducer
# date: 15/12/2020

from iostream._loader import Loader
from iostream._task_usdeur_loader import TaskUsdEurLoader
from iostream._task_gbpusd_loader import TaskGbpUsdLoader

__all__ = [
    'Loader',
    'TaskGbpUsdLoader',
    'TaskUsdEurLoader'
]
