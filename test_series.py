import unittest
from series import fibonacci, lucas, sum_series, sum_series_two

class TestIt(unittest.TestCase):
    def test_1(self):
        self.assertEquals(fibonacci(3), 2)

    def test_2(self):
        self.assertEquals(lucas(5), 11)

    def test_3(self):
        self.assertEquals(sum_series(3), 2)

    def test_4(self):
        self.assertEquals(sum_series(5, 2, 1), 11)  

    def test_5(self):
        self.assertEquals(sum_series_two(3), 2)

    def test_6(self):
        self.assertEquals(sum_series_two(5, 2, 1), 11)  

if __name__ == '__main__':
    unittest.main()