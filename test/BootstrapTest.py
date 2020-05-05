import unittest

from Sampling.Bootstrap import Bootstrap


class BootstrapTest(unittest.TestCase):

    def setUp(self) -> None:
        self.smallSample = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.largeSample = []
        for i in range(1000000):
            self.largeSample.append(i)

    def test_SmallSample(self):
        bootstrap = Bootstrap(self.smallSample, 1)
        sample = ["3", "10", "2", "5", "2", "8", "8", "8", "7", "4"]
        self.assertEquals(sample, bootstrap.getSample())

    def test_LargeSample(self):
        bootstrap = Bootstrap(self.largeSample, 1)
        sample = bootstrap.getSample()
        sampleSet = set()
        sampleSet.update(sample)
        self.assertAlmostEqual(len(sampleSet) / 1000000.0, 0.632, 3)


if __name__ == '__main__':
    unittest.main()
