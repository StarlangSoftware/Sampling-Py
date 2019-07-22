import random


class Bootstrap:
    def __init__(self, instanceList: list, seed: int):
        random.seed(seed)
        N = len(instanceList)
        self.instanceList = []
        for i in range(N):
            self.instanceList.append(instanceList[random.randint(0, N - 1)])

    def getSample(self) -> list:
        return self.instanceList
