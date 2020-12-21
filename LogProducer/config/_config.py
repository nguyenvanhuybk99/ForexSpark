# author: Huy.Nguyen
# institute: Hanoi University of Science and Technology
# file name: _config.py
# project name: LogProducer
# date: 15/12/2020

from abc import ABCMeta, abstractmethod


class Config(metaclass=ABCMeta):

    @abstractmethod
    def name(self) -> str:
        pass
