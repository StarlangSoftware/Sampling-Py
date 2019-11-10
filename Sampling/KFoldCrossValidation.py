from Sampling.CrossValidation import CrossValidation
import random


class KFoldCrossValidation(CrossValidation):

    __instanceList: list
    __N: int

    """
    A constructor of KFoldCrossValidation class which takes a sample as an array of instances, a K (K in K-fold
    cross-validation) and a seed number, then shuffles the original sample using this seed as random number.

    PARAMETERS
    ----------
    instanceList : list
        Original sample
    K : int
        K in K-fold cross-validation
    seed : int
        Random number to create K-fold sample(s)
    """
    def __init__(self, instanceList: list, K: int, seed: int):
        self.__instanceList = instanceList
        random.seed(seed)
        random.shuffle(instanceList)
        self.__N = len(instanceList)
        self.K = K

    """
    getTrainFold returns the k'th train fold in K-fold cross-validation.

    PARAMETERS
    ----------
    k : int 
        index for the k'th train fold of the K-fold cross-validation
        
    RETURNS
    -------
    list
        Produced training sample
    """
    def getTrainFold(self, k: int) -> list:
        trainFold = []
        for i in range((k * self.__N) // self.K):
            trainFold.append(self.__instanceList[i])
        for i in range(((k + 1) * self.__N) // self.K):
            trainFold.append(self.__instanceList[i])
        return trainFold

    """
    getTestFold returns the k'th test fold in K-fold cross-validation.

    PARAMETERS
    ----------
    k : int
        index for the k'th test fold of the K-fold cross-validation
        
    RETURNS
    -------
    list
        Produced testing sample
    """
    def getTestFold(self, k: int) -> list:
        testFold = []
        for i in range((k * self.__N) // self.K, ((k + 1) * self.__N) // self.K):
            testFold.append(self.__instanceList[i])
        return testFold
