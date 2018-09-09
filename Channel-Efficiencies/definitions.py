import numpy as np 

K = 100

class Transmitter:
    ''' 
        All transmitter types are created using this class. 
        Class contains power and channel_gain definitions, 
        but no methods of its own. Think Structure
    '''
    
    def __init__ (self):
        # power related definitions 
        self.max_power_levels = K
        self.max_power        = 1 
        
        # uniformly initialising the power across all levels 
        self.power = []
        temp = []
        for i in range (self.max_power_levels):
            for j in range (self.max_power_levels):
                temp.append (self.max_power/self.max_power_levels)
            self.power.append (temp)
            temp = []
        self.power = np.array (self.power)
        # channel_gain related definitions 
        self.channel_gain = np.random.exponential (scale=5, size=[self.max_power_levels,self.max_power_levels])
        self.noise        = np.random.uniform (low=0, high=8)

def SINR (transmitter):
    ''' 
        Returns the SINR value of the transmitter object passed as argument.
        Computed as standard formula.
        RETURN VALUE: numpy array of floats
    ''' 
    SINR = []
    # defining the noise level of the channel in question 
    noise_level = transmitter.noise ** 2
        
    ''' 
    The channel_gain is calculated as follows: 
    p_i * g_ii divided by the noise_level and some funky stuff.
    This is the product of each column of g's against the power levels 
    '''
    # this is the funky bit
    channel_gain = []
    for col_g in np.vsplit (transmitter.channel_gain, transmitter.max_power_levels):
        channel_gain.append (np.dot(transmitter.power, col_g.flatten()))
        
    # composing the SINR now 
    for index in range (0,transmitter.max_power_levels):
        numerator = transmitter.power [index][index] * channel_gain [index]
        SINR.append (
            (  numerator / (noise_level + (channel_gain[index] - numerator)) ) 
        )
    return np.array(SINR)
# end of SINR function definition 

def utility_func (transmitter):
    ''' 
    This function calculates the individual inst. utility function, 
    and returns a corresponding list of the same. 
    RETURN TYPE: numpy list of floats 
    '''
    # extracting the sinr values corresponding to a transmitter 
    sinr = SINR (transmitter)    

    # defining the utility function as a simple sigmoid of the sinr values 
    utility = np.exp (sinr) / (1 + np.exp(sinr))
    return utility / transmitter.power 

def sumEnergyEfficiency (utility_list, transmitter):
    ''' This function defines the w - sumEE. ''' 
    sumEE = np.array ([transmitter.power[index] * transmitter.channel_gain[index][index] for index in range (transmitter.max_power_levels)])
    sumEE = np.sum (sumEE)
    return sumEE
    
def Expectation (transmitter):
    # defining the prob. dist and the sumEE for the weighted sum 
    w = sumEnergyEfficiency (utility_func (transmitter), transmitter)
    p_dist = np.random.exponential (scale=5, size=(transmitter.max_power_levels, transmitter.max_power_levels))

    # this is the closest we can get to the expectation values 
    return np.sum (np.dot (p_dist, w))

