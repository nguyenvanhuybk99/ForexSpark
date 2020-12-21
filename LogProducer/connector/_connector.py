# author: Huy.Nguyen
# institute: Hanoi University of Science and Technology
# file name: _connector.py
# project name: LogProducer
# date: 15/12/2020

from abc import ABCMeta, abstractmethod

from config import Config


class Connector(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def getNewInstance(cls, config: Config):
        pass

    @abstractmethod
    def submit(self, payload: str):
        pass
