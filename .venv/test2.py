import unittest
import main




class GuessTest(unittest.TestCase):
    def test_setup(self):
        print('test start !!')

    def test_guess_input(self):
        res = main.guess_number(5,5)
        self.assertTrue(res)

    def test_guess_wrong(self):
        res = main.guess_number(5,0)
        self.assertFalse(res)

    def test_guess_outrangenumber(self):
        res = main.guess_number(11,7)
        self.assertFalse(res,'just input number from 1 - 10')





if __name__ == '__main':
    unittest.main()