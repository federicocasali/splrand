""" Module to compute probability density functions
"""
import numpy
from scipy.interpolate import InterpolatedUnivariateSpline

class ProbabilityDensityFunction:
    """ Class re-building the probability density function \
        from the input data.
    """
    def __init__(self,x,y,order=3):
        """ The constructor takes as input some points wich sample \
            the distribution and the order of polinomial approximation \
            (spline) to be done.
        """
        self._s=InterpolatedUnivariateSpline(x,y,k=order)
        ycdf=numpy.array([self._s.integral(x[0],x[i]) for i in range(len(x))])
        self.cdf=InterpolatedUnivariateSpline(x,ycdf)
        self.ppf=InterpolatedUnivariateSpline(ycdf,x)

    def prob(self,a,b):
        """ Returns probability in the interval [a,b]
        """
        return self.cdf(b)-self.cdf(a)

    def rnd(self,size=50):
        """ Returns a numpy.array of *size* random variables \
            distributed uniformly according to the pdf approximated with spline
        """
        return self.ppf(np.random.uniform(size=size))

