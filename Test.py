import unittest as ut
import numpy as np
import Pephon as pt
class CalcTest(ut.TestCase):
    def setUp(self):
        self.mk=pt.MyClass()
    def test_add(self):
        self.assertEqual(self.mk.Return_k(self.mk.Progression(3,9,10),9),432)
        
if __name__ == '__main__':
    import xmlrunner
    runner=xmlrunner.XMLTestRunner(output='test-reports')
    ut.main(testRunner=runner)
    ut.main()

