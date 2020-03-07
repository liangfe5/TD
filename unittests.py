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




    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')
    #
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()