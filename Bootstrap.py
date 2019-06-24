class Bootstrap:
    def __init__(self, instanceList, seed):
        N = len(instanceList)
        self.instanceList = []
        for i in range(0, N - 1):
            self.instanceList.append()

    def getSample(self):
        return self.instanceList