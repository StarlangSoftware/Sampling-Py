import unittest

from Sampling.KFoldCrossValidation import KFoldCrossValidation


class KFoldCrossValidationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.smallSample = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.largeSample = []
        for i in range(1000):
            self.largeSample.append(i)

    def test_SmallSample10Fold(self):
        kFoldCrossValidation = KFoldCrossValidation(self.smallSample, 10, 1)
        expected1 = ["7"]
        self.assertEquals(expected1, kFoldCrossValidation.getTestFold(0))

    def test_SmallSample5Fold(self):
        kFoldCrossValidation = KFoldCrossValidation(self.smallSample, 5, 1)
        expected2 = ["7", "9"]
        self.assertEquals(expected2, kFoldCrossValidation.getTestFold(0))

    def test_SmallSample2Fold(self):
        kFoldCrossValidation = KFoldCrossValidation(self.smallSample, 2, 1)
        expected3 = ["7", "9", "10", "8", "6"]
        self.assertEquals(expected3, kFoldCrossValidation.getTestFold(0))

    def test_LargeSample10Fold(self):
        kFoldCrossValidation = KFoldCrossValidation(self.largeSample, 10, 1)
        for i in range(10):
            items = set()
            trainFold = kFoldCrossValidation.getTrainFold(i)
            testFold = kFoldCrossValidation.getTestFold(i)
            items.update(trainFold)
            items.update(testFold)
            self.assertEquals(100, len(testFold))
            self.assertEquals(900, len(trainFold))
            self.assertEquals(1000, len(items))

    def test_LargeSample5Fold(self):
        kFoldCrossValidation = KFoldCrossValidation(self.largeSample, 5, 1)
        for i in range(5):
            items = set()
            trainFold = kFoldCrossValidation.getTrainFold(i)
            testFold = kFoldCrossValidation.getTestFold(i)
            items.update(trainFold)
            items.update(testFold)
            self.assertEquals(200, len(testFold))
            self.assertEquals(800, len(trainFold))
            self.assertEquals(1000, len(items))

    def test_LargeSample2Fold(self):
        kFoldCrossValidation = KFoldCrossValidation(self.largeSample, 2, 1)
        for i in range(2):
            items = set()
            trainFold = kFoldCrossValidation.getTrainFold(i)
            testFold = kFoldCrossValidation.getTestFold(i)
            items.update(trainFold)
            items.update(testFold)
            self.assertEquals(500, len(testFold))
            self.assertEquals(500, len(trainFold))
            self.assertEquals(1000, len(items))


if __name__ == '__main__':
    unittest.main()
