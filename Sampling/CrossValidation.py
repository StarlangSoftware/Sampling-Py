from abc import abstractmethod


class CrossValidation(object):

    K: int

    @abstractmethod
    def getTrainFold(self, k: int) -> list:
        pass

    @abstractmethod
    def getTestFold(self, k: int) -> list:
        pass