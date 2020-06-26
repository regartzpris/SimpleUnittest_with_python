import unittest
import main



class TestMain(unittest.TestCase):
    def test_setup(self):
        print('test start !!')
        
    def test_do(self):
        num=4
        res = main.do(num)
        self.assertEqual(res,7)

    def test_do2(self):
        num ='kjhkhk'
        res = main.do(num)
        # self.assertEqual(res,TypeError)
        self.assertIsInstance(res,TypeError)


    def test_do3(self):
        num=None
        res=main.do(num)
        self.assertEqual(res,'please insert number')

    def test_do4(self):
        num=''
        res=main.do(num)
        self.assertEqual(res,'please insert number')


if __name__ == '__main__':
    unittest.main()