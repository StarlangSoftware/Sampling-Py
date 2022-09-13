import unittest

from Sampling.StratifiedKFoldCrossValidation import StratifiedKFoldCrossValidation


class StratifiedKFoldCrossValidationTest(unittest.TestCase):

    def setUp(self) -> None:
        inputClass1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        inputClass2 = ["11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
        self.smallSample = [inputClass1, inputClass2]
        class1 = []
        for i in range(1000):
            class1.append(i)
        class2 = []
        for i in range(3000):
            class2.append(1000 + i)
        class3 = []
        for i in range(5000):
            class3.append(4000 + i)
        self.largeSample = [class1, class2, class3]

    def test_SmallSample10Fold(self):
        stratifiedKFoldCrossValidation = StratifiedKFoldCrossValidation(self.smallSample, 10, 1)
        expected1 = ["7", "22", "16"]
        self.assertEqual(expected1, stratifiedKFoldCrossValidation.getTestFold(0))

    def test_SmallSample5Fold(self):
        stratifiedKFoldCrossValidation = StratifiedKFoldCrossValidation(self.smallSample, 5, 1)
        expected2 = ["7", "9", "22", "16", "28", "30"]
        self.assertEqual(expected2, stratifiedKFoldCrossValidation.getTestFold(0))

    def test_SmallSample2Fold(self):
        stratifiedKFoldCrossValidation = StratifiedKFoldCrossValidation(self.smallSample, 2, 1)
        expected3 = ["7", "9", "10", "8", "6", "22", "16", "28", "30", "20", "11", "27", "12", "26", "17"]
        self.assertEqual(expected3, stratifiedKFoldCrossValidation.getTestFold(0))

    def test_LargeSample10Fold(self):
        stratifiedKFoldCrossValidation = StratifiedKFoldCrossValidation(self.largeSample, 10, 1)
        for i in range(10):
            items = set()
            trainFold = stratifiedKFoldCrossValidation.getTrainFold(i)
            testFold = stratifiedKFoldCrossValidation.getTestFold(i)
            items.update(trainFold)
            items.update(testFold)
            self.assertEqual(900, len(testFold))
            self.assertEqual(8100, len(trainFold))
            self.assertEqual(9000, len(items))
            trainCounts = [0, 0, 0]
            for integer in trainFold:
                if integer < 1000:
                    trainCounts[0] = trainCounts[0] + 1
                elif integer < 4000:
                    trainCounts[1] = trainCounts[1] + 1
                else:
                    trainCounts[2] = trainCounts[2] + 1
            self.assertEqual(900, trainCounts[0])
            self.assertEqual(2700, trainCounts[1])
            self.assertEqual(4500, trainCounts[2])
            testCounts = [0, 0, 0]
            for integer in testFold:
                if integer < 1000:
                    testCounts[0] = testCounts[0] + 1
                elif integer < 4000:
                    testCounts[1] = testCounts[1] + 1
                else:
                    testCounts[2] = testCounts[2] + 1
            self.assertEqual(100, testCounts[0])
            self.assertEqual(300, testCounts[1])
            self.assertEqual(500, testCounts[2])

    def test_LargeSample5Fold(self):
        stratifiedKFoldCrossValidation = StratifiedKFoldCrossValidation(self.largeSample, 5, 1)
        for i in range(5):
            items = set()
            trainFold = stratifiedKFoldCrossValidation.getTrainFold(i)
            testFold = stratifiedKFoldCrossValidation.getTestFold(i)
            items.update(trainFold)
            items.update(testFold)
            self.assertEqual(1800, len(testFold))
            self.assertEqual(7200, len(trainFold))
            self.assertEqual(9000, len(items))
            trainCounts = [0, 0, 0]
            for integer in trainFold:
                if integer < 1000:
                    trainCounts[0] = trainCounts[0] + 1
                elif integer < 4000:
                    trainCounts[1] = trainCounts[1] + 1
                else:
                    trainCounts[2] = trainCounts[2] + 1
            self.assertEqual(800, trainCounts[0])
            self.assertEqual(2400, trainCounts[1])
            self.assertEqual(4000, trainCounts[2])
            testCounts = [0, 0, 0]
            for integer in testFold:
                if integer < 1000:
                    testCounts[0] = testCounts[0] + 1
                elif integer < 4000:
                    testCounts[1] = testCounts[1] + 1
                else:
                    testCounts[2] = testCounts[2] + 1
            self.assertEqual(200, testCounts[0])
            self.assertEqual(600, testCounts[1])
            self.assertEqual(1000, testCounts[2])

    def test_LargeSample2Fold(self):
        stratifiedKFoldCrossValidation = StratifiedKFoldCrossValidation(self.largeSample, 2, 1)
        for i in range(2):
            items = set()
            trainFold = stratifiedKFoldCrossValidation.getTrainFold(i)
            testFold = stratifiedKFoldCrossValidation.getTestFold(i)
            items.update(trainFold)
            items.update(testFold)
            self.assertEqual(4500, len(testFold))
            self.assertEqual(4500, len(trainFold))
            self.assertEqual(9000, len(items))
            trainCounts = [0, 0, 0]
            for integer in trainFold:
                if integer < 1000:
                    trainCounts[0] = trainCounts[0] + 1
                elif integer < 4000:
                    trainCounts[1] = trainCounts[1] + 1
                else:
                    trainCounts[2] = trainCounts[2] + 1
            self.assertEqual(500, trainCounts[0])
            self.assertEqual(1500, trainCounts[1])
            self.assertEqual(2500, trainCounts[2])
            testCounts = [0, 0, 0]
            for integer in testFold:
                if integer < 1000:
                    testCounts[0] = testCounts[0] + 1
                elif integer < 4000:
                    testCounts[1] = testCounts[1] + 1
                else:
                    testCounts[2] = testCounts[2] + 1
            self.assertEqual(500, testCounts[0])
            self.assertEqual(1500, testCounts[1])
            self.assertEqual(2500, testCounts[2])


if __name__ == '__main__':
    unittest.main()
