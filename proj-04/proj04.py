#!/usr/bin/env

"""
EE 381 Project 04
Name: David Taitingfong
I.D.: 016695521
Start date: 03-25-2019
End date:   04-08-2019

Description:
    Simulation of Binomial distributions with a bar graph.
"""


import random
import math
from matplotlib import pyplot


def main():
    '''Simulation of the Binomial Distribution'''
    
    n = 5       # Number of trials
    y = 3       # Number of wanted success in trials
    p = 0.7     # Proability of success
    Y = []      # Record  of binomial trials
    z = 0       # Accumulator for sum of 3
    X = 0       # Accumulator of all trials
    N = 600000  # Number of experiments
    R = []      # Every outcome to calculate variance
    b = [0 for val in range(n+1)] # Counters for sums

    '''
    Part 1: calculate the probability of getting exactly three successes
    '''
    i = 0
    while i < N:
        j = 0
        while j < n:
            r = random.uniform(0, 1)
            if r < p:
                x = 1   # Bernoulli
            else:       # Random
                x = 0   # Variables
            Y.append(x)
            j += 1
        
        b[sum(Y)] += 1
        R.append(sum(Y))    # Add that sum to R
        X += sum(Y)         # Accrue X with the sum
        if sum(Y) == y:     # Check if the sum = the # of successes we want
            z += 1
        Y.clear()   # Empty list for next run
        i += 1
    
    p = z / N   # Times we got a sum 3 divided by total num of runs
    ave = X / N # Average sum across all trials

    print("Probability of 3 successes in 5 trials: {:.3f}".format(p))
    print("The average is {:.3f}".format(ave))

    '''Part 2 - Get standard deviation'''
    q = 0   # Accumulator for variance calculation
    for k in R:
        q += (k-ave)**2
    q /= N
    sigma = math.sqrt(q)
    print("Standard deviation: {:.3f}".format(sigma))

    '''Part 3 - Plot'''
    a = [val for val in range(n+1)]   # x-axis
    
    b = [(val/N) for val in b]
    pyplot.bar(a, b, 1, color=['#222222', '#cc6672',
                               '#d4a76a', '#496d89',
                               '#6cb359', '#999999'])
    pyplot.title('Bar Graph of Binomial PMF', loc='right')
    pyplot.ylabel('Probabilities', fontsize='x-large')
    pyplot.show()


if __name__ == "__main__":
    main()
