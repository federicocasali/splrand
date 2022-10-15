""" Test for assignment_basic_4.py
"""
import unittest
import numpy
import sys

try:
    from splrand.pdf import ProbabilityDensityFunction
except ModuleNotFoundError as e:
    print(e)
    for l in sys.path:
        print(l)
class TestProbabilityDensityFunction(unittest.TestCase):

    def test_norm(self):
        x=numpy.linspace(0,1,100)
        y=2.*x
        a=ProbabilityDensityFunction(x,y)
        d=a.cdf(x[-1])-a.cdf(x[0])
        print(f"{a.cdf(x[-1])} - {a.cdf(x[0])} = {d} ")
        self.assertAlmostEqual(d,1.)

if __name__=='__main__':
    unittest.main(exit=False)
