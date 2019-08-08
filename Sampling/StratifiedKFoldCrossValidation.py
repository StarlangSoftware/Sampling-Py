from Sampling.KFoldCrossValidation import KFoldCrossValidation
import random


class StratifiedKFoldCrossValidation(KFoldCrossValidation):

    def __init__(self, instanceLists: list, K: int, seed: int):
        self.instanceLists = instanceLists
        self.N = []
        for i in range(len(instanceLists)):
            random.seed(seed)
            random.shuffle(instanceLists[i])
            self.N.append(len(instanceLists[i]))
        self.K = K

    def getTrainFold(self, k: int) -> list:
        trainFold = []
        for i in range(len(self.N)):
            for j in range((k * self.N[i]) // self.K):
                trainFold.append(self.instanceLists[i][j])
            for j in range(((k + 1) * self.N[i]) // self.K, self.N[i]):
                trainFold.append(self.instanceLists[i][j])
        return trainFold

    def getTestFold(self, k: int) -> list:
        testFold = []
        for i in range(len(self.N)):
            for j in range((k * self.N[i]) // self.K, ((k + 1) * self.N[i]) // self.K):
                testFold.append(self.instanceLists[i][j])
        return testFold
