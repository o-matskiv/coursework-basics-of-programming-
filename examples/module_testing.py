import unittest
from Ward import *


class TestWard(unittest.TestCase):
    def install(self):
        self.Shirley = Ward('Shirley')
        self.Shirley2 = Ward('Shirley')
        self.Abbey = Ward('Abbey')

    def test_istance(self):
        self.assertIsInstance(self.Abbey, Ward)
        ok = False
        try:
            self.assertIsInstance(self.Shirley, Array)
        except:
            ok = True
        assert(ok)

    def test_price(self):
        self.Abbey.set_price(345)
        self.assertEqual(self.Abbey.get_price(), 345)
        ok = False
        try:
            self.Shirley.set_price('price')
        except:
            ok = True
        assert(ok)

    def test_school(self):
        self.Abbey.add_school('School #2')
        self.assertEqual(self.Abbey.get_number_of_schools(), 1)
        ok = False
        try:
            self.Shirley.add_school(456)
        except:
            ok = True
        assert(ok)

    def test_equal(self):
        self.assertEqual(self.Shirley, self.Shirley2)
        ok = False
        try:
            self.assertEqual(self.Shirley, self.Abbey)
        except:
            ok = True
        assert(ok)

    def test_crimes(self):
        self.Abbey.add_number_crimes(3456)
        self.assertEqual(self.Abbey.get_number_of_crimes(), 3456)
        try:
            self.Shirley.add_number_crimes('456')
        except:
            ok = True
        assert(ok)


if __name__ == '__main__':
    print('Testing Ward...', end='')
    tst = TestWard()
    tst.install()
    tst.test_istance()
    tst.test_price()
    tst.test_school()
    tst.test_equal()
    tst.test_crimes()
    print('Done')
