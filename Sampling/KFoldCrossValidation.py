from Sampling.CrossValidation import CrossValidation
import random


class KFoldCrossValidation(CrossValidation):

    __instance_list: list
    __N: int

    def __init__(self,
                 instance_list: list,
                 K: int,
                 seed: int):
        """
        A constructor of KFoldCrossValidation class which takes a sample as an array of instances, a K (K in K-fold
        cross-validation) and a seed number, then shuffles the original sample using this seed as random number.

        PARAMETERS
        ----------
        instance_list : list
            Original sample
        K : int
            K in K-fold cross-validation
        seed : int
            Random number to create K-fold sample(s)
        """
        self.__instance_list = instance_list
        random.seed(seed)
        random.shuffle(instance_list)
        self.__N = len(instance_list)
        self.K = K

    def getTrainFold(self, k: int) -> list:
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
        train_fold = []
        for i in range((k * self.__N) // self.K):
            train_fold.append(self.__instance_list[i])
        for i in range(((k + 1) * self.__N) // self.K, self.__N):
            train_fold.append(self.__instance_list[i])
        return train_fold

    def getTestFold(self, k: int) -> list:
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
        test_fold = []
        for i in range((k * self.__N) // self.K, ((k + 1) * self.__N) // self.K):
            test_fold.append(self.__instance_list[i])
        return test_fold
