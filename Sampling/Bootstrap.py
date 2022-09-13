import random


class Bootstrap:

    __instance_list: list

    def __init__(self,
                 instance_list: list,
                 seed: int):
        """
        A constructor of Bootstrap class which takes a sample an array of instances and a seed number, then creates a
        bootstrap sample using this seed as random number.

        PARAMETERS
        ----------
        instance_list : list
            Original sample
        seed : int
            Random number to create boostrap sample
        """
        random.seed(seed)
        N = len(instance_list)
        self.__instance_list = []
        for i in range(N):
            self.__instance_list.append(instance_list[random.randint(0, N - 1)])

    def getSample(self) -> list:
        """
        getSample returns the produced bootstrap sample.

        RETURNS
        -------
        list
            Produced bootstrap sample
        """
        return self.__instance_list
