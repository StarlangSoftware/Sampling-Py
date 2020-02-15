import random


class Bootstrap:

    __instanceList: list

    def __init__(self, instanceList: list, seed: int):
        """
        A constructor of Bootstrap class which takes a sample an array of instances and a seed number, then creates a
        bootstrap sample using this seed as random number.

        PARAMETERS
        ----------
        instanceList : list
            Original sample
        seed : int
            Random number to create boostrap sample
        """
        random.seed(seed)
        N = len(instanceList)
        self.__instanceList = []
        for i in range(N):
            self.__instanceList.append(instanceList[random.randint(0, N - 1)])

    def getSample(self) -> list:
        """
        getSample returns the produced bootstrap sample.

        RETURNS
        -------
        list
            Produced bootstrap sample
        """
        return self.__instanceList
