from Sampling.KFoldCrossValidation import KFoldCrossValidation
import random


class StratifiedKFoldCrossValidation(KFoldCrossValidation):

    """
    A constructor of StratifiedKFoldCrossValidation class which takes as set of class samples as an array of array of
    instances, a K (K in K-fold cross-validation) and a seed number, then shuffles each class sample using the
    seed number.

    PARAMETERS
    ----------
    instanceLists : list
        Original class samples. Each element of the this array is a sample only from one class.
    K : int
        K in K-fold cross-validation
    seed : int
        Random number to create K-fold sample(s)
    """
    def __init__(self, instanceLists: list, K: int, seed: int):
        self.instanceLists = instanceLists
        self.N = []
        for i in range(len(instanceLists)):
            random.seed(seed)
            random.shuffle(instanceLists[i])
            self.N.append(len(instanceLists[i]))
        self.K = K

    """
    getTrainFold returns the k'th train fold in K-fold stratified cross-validation.

    PARAMETERS
    ----------
    k : int
        index for the k'th train fold of the K-fold stratified cross-validation
        
    RETURNS
    -------
    list
        Produced training sample
    """
    def getTrainFold(self, k: int) -> list:
        trainFold = []
        for i in range(len(self.N)):
            for j in range((k * self.N[i]) // self.K):
                trainFold.append(self.instanceLists[i][j])
            for j in range(((k + 1) * self.N[i]) // self.K, self.N[i]):
                trainFold.append(self.instanceLists[i][j])
        return trainFold

    """
    getTestFold returns the k'th test fold in K-fold stratified cross-validation.

    PARAMETERS
    ----------
    k : int
        index for the k'th test fold of the K-fold stratified cross-validation
        
    RETURNS
    -------
    list
        Produced testing sample
    """
    def getTestFold(self, k: int) -> list:
        testFold = []
        for i in range(len(self.N)):
            for j in range((k * self.N[i]) // self.K, ((k + 1) * self.N[i]) // self.K):
                testFold.append(self.instanceLists[i][j])
        return testFold
