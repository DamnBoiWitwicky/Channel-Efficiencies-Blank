from definitions import * 

def main():
    t = Transmitter()
    print ("The SINR values are: ", SINR(t), "\n")
    print ('The utility function evaluates to: ',utility_func(t), '\n')
    print ('The sum of the E-energy is:',sumEnergyEfficiency(utility_func(t), t), '\n')
    print ('Expectation of the transmitter is: ', Expectation(t), '\n')

if __name__ == '__main__':
    main()
    