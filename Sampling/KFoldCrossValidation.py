from Sampling import CrossValidation
import random


class KFoldCrossValidation(CrossValidation):
    def __init__(self, instanceList: list, K: int, seed: int):
        self.instanceList = instanceList
        random.seed(seed)
        random.shuffle(instanceList)
        self.N = len(instanceList)
        self.K = K

    def getTrainFold(self, k: int) -> list:
        trainFold = []
        for i in range((k * self.N) // self.K):
            trainFold.append(self.instanceList[i])
        for i in range(((k + 1) * self.N) // self.K):
            trainFold.append(self.instanceList[i])
        return trainFold

    def getTestFold(self, k: int) -> list:
        testFold = []
        for i in range((k * self.N) // self.K, ((k + 1) * self.N) // self.K):
            testFold.append(self.instanceList[i])
        return testFold
