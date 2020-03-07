import unittest
from ThirtySecondsFormatter import ThirtySecondsFormatter

class TestTD(unittest.TestCase):
    def test_zero(self):
        test = ThirtySecondsFormatter()
        result = test.convert(0)
        self.assertEqual('00-00', result)

    def test_int(self):
        test = ThirtySecondsFormatter()
        result = test.convert(50)
        self.assertEqual('50-00', result)

    def test_given(self):
        test = ThirtySecondsFormatter()
        result = test.convert(105.25)
        result2 = test.convert(9.03125)
        self.assertEqual('105-08', result)
        self.assertEqual('105-08', result)

    def test_negative(self):
        test = ThirtySecondsFormatter()
        result = test.convert(-0.50)
        self.assertEqual('-00-16', result)

if __name__ == '__main__':
    unittest.main()