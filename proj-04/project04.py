#!/usr/bin/env

"""
EE 381 Project 04
Name: David Taitingfong
I.D.: 016695521
Start date: 03-25-2019
End date:   0?-??-2019

Description:
    Simulation of Binomial distributions with a bar graph.
"""

import random
import math
from matplotlib import pyplot

def part_one():
    '''Calculate the probability of exactly three successes'''

    n = 5       # Number of trials
    y = 3       # Number of success in trials
    p = 0.7     # Proability of success
    Y = []      # Record of binomial trials

    z = 0       # Accumulator for sum of 3
    X = 0       # Accumulator of all trials

    N = 600000  # Number of experiments
    R = []      # Record every outcome to calculate variance
    b = [0 for val in range(n+1)] # Counters for sum


    '''Conduct experiment'''
    i = 0
    while i < N:
        j = 0
        # Conduct trials
        while j < n:
            r = random.uniform(0, 1)

            # Bernoulli Random Variables
            x = 1 if r < p else 0
            
            Y.append(x)
            j += 1
        
        b[sum(Y)] += 1      # Sums counter
        R.append(sum(Y))    # Add that sum to R[]
        X += sum(Y)         # Accrue X with the sum
        if sum(Y) == y:     # Check if the sum = the # of successes we want
            z += 1
        Y.clear()   # Empty list for next run
        i += 1
    '''End of experiment'''
    
    p = z / N       # Times we got a sum 3 divided by total num of runs
    ave = X / N     # Average sum across all trials

    print("Probability of 3 successes in 5 trials: {:.3f}".format(p))
    print("The average is {:.3f}".format(ave))

    '''Get standard deviation -> transfer to part02 later'''
    q = 0   # Accumulator for variance calculation
    for k in R:
        q += (k - ave)**2
    q /= N
    sigma = math.sqrt(q)
    print("Standard deviation: {:.3f}".format(sigma))

    print("\nExpected mean: {:.3f}".format(n * p))
    print("Standard deviation: {:.3f}".format(math.sqrt(n * p * (1 - p))))

    '''Part 03 - Plot'''
    a = [val for val in range(n+1)]     # x-axis 
    b = [(val/N) for val in b]          # y-axis

    pyplot.bar(a, b, 1, color=['#222222', '#cc6672',
                               '#d4a76a', '#496d89',
                               '#6cb359', '#999999'])
    pyplot.title('Bar Graph of Binomial PMF', loc='right')
    pyplot.ylabel('Probabilities', fontsize='x-large')
    pyplot.show()


def main():
    part_one()


if __name__ == "__main__":
    main()
