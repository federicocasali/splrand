import numpy
from scipy.interpolate import InterpolatedUnivariateSpline

class ProbabilityDensityFunction:
    def __init__(self,x,y,order=3):
        self._s=InterpolatedUnivariateSpline(x,y,k=order)
        ycdf=numpy.array([self._s.integral(x[0],x[i]) for i in range(len(x))])
        self.cdf=InterpolatedUnivariateSpline(x,ycdf)
        self.ppf=InterpolatedUnivariateSpline(ycdf,x)

    def prob(self,a,b):
        return self.cdf(b)-self.cdf(a)

    def rnd(self,size=50):
        return self.ppf(np.random.uniform(size=size))

