from numpy.random import uniform, random, exponential
from numpy import sort, append 
from definitions import Transmitter

class ThresholdFunction:
    def __init__ (self, x_range, y_range):
        self.threshold  = uniform (low=0, high=random())
        self.alpha      = random ()
        self.x_range    = x_range
        self.y_range    = y_range 
    def func (self, x):
        if (x < self.threshold):
            return 0
        else:
            return (self.alpha * self.threshold ** 2) / x
    def setThreshold (self, threshold):
        self.threshold = threshold
    def neighbourhood_threshold (self, epsilon, size):
        ''' 
            epsilon defines the size of the neighbourhood 
            we return a list containing points in this neighbourhood 
        ''' 
        neighbourhood = uniform (low=self.threshold-epsilon, high=self.threshold+epsilon, size=size)
        append (neighbourhood, self.threshold)
        return sort (neighbourhood)
    
def MonteCarloIntegral (function, x_range, y_range, num_points=10_000):
    # creating the random points 

    x_points = uniform (low=x_range [0], high=x_range[1], size=(num_points,))
    y_points = uniform (low=y_range [0], high=y_range[1], size=(num_points,))

    count = 0
    for x, y in zip (x_points, y_points):
        point = function (x)
        if (point < y and point > 0 and y > 0):
            count += 1
        elif point < 0 and y < 0 and point > y:
            count -= 1
    return count * (x_range[1]-x_range[0]) * (y_range[1]-y_range[0]) / num_points

def weightedMCI (list, x_range, y_range, num_points=10_000):
    function = lambda x: x*exponential (scale=5)
    return (MonteCarloIntegral(
        function, x_range, y_range, num_points
    ))

    