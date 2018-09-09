 # this is the file that defines the algorithm 
# that calculates the best thresholds for the functions.

import definitions as d
import functions as f 
import numpy as np 
from numpy.random import exponential

# creating the transmitter to work with 
mitter = d.Transmitter ()

# creating a vector of threshold functions
threshold_vector = [f.ThresholdFunction() for _ in range (d.K)]

# defining the number of iterations 
ITER_MAX = 10_000

for threshold_func in threshold_vector: 
    # calculating the old expectations 
    # and storing the old threshold 
    old_threshold = threshold_func.threshold
    area_old = f. weightedMCI ( d.sumEnergyEfficiency(d.utility_func(t), t) )
    
    while abs (threshold_func.threshold - old_threshold) >= 10e-5:
        potentials = threshold_func.neighbourhood_threshold (epsilon=0.5, size=20)
        temp_objects = [d.Transmitter for _ in range (20)]
        
        # calculating the new thresholds 
        utilities = list (map, d.utility_func, temp_objects)
        new_areas = list (map (d.sumEnergyEfficiency,utilities, temp_objects))
        
        # getting the best area 
        area_new = new_areas [np.argmax (new_areas)]
        threshold_func.threshold = area_new

