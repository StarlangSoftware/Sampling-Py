import abc
from abc import abstractmethod


class CrossValidation(abc):

    @abstractmethod
    def getTrainFold(self, k: int) -> list:
        pass

    @abstractmethod
    def getTestFold(self, k: int) -> list:
        pass