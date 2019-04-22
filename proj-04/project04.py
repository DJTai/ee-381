#!/usr/bin/env

"""
EE 381 Project 04
Name: David Taitingfong
I.D.: 016695521
Start date: 04-08-2019
End date:   04-10-2019

EXERCISES
Exercise 1: n = 5 and p = 0.7, P({X=3}) = 5!/((3!)2!)(0.7^3)(0.3^2) = 0.3087
Exercise 2:
    n = 5, p = 0.7
    mu = np = 3.5
    sigma = sqrt(npq) = sqrt(5*0.7*0.3) = 1.025
"""

import math
import random
from matplotlib import pyplot

def main():
    """Stuff"""

    def parameters():
        p = float(input("Enter the probability of success: "))
        n = int(input("Enter the number of trials: "))
        print("To determine the probability of success over an interval, " +
                "you'll be asked to enter the low and high values.")

        y_low = int(input("Enter the low value: "))
        y_high = int(input("Enter the high value: "))

        return p, n, y_low, y_high


    def binomial(p: float, n: int, y_lo: int, y_hi: int):
        Y: list = []    # Record  of binomial trials
        N = 600000      # Number of experiments
        b = [0 for val in range(n+1)]
        prob = 0
        X = 0
        R = []    # Records

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
            R.append(sum(Y))
            X += sum(Y)
            Y.clear()   # Empty list for next run
            i += 1

        b = [(val/N) for val in b]

        for val in range(y_lo, y_hi + 1):
            prob += b[val]

        print("Probability of success from {} to {}: ".format(y_lo, y_hi), end='')
        print("{0:.4f}".format(prob))
        print("Average: {0:.4f}".format(X/N))

        q = 0
        for k in R:
            q += (k-(X/N))**2
        q /= N
        sigma = math.sqrt(q)
        print("Sigma: {0:.3f}".format(sigma))

        return b


    def histogram(trials: int, b) -> None:
        w = 1
        x = []
        for i in range(trials + 1):
            x.append(i)

        pyplot.bar(x, b, w, color=['#222222', '#cc6672',
                               '#d4a76a', '#496d89',
                               '#6cb359', '#999999'])
        pyplot.title('Bar Graph of Binomial PMF', loc='right')
        pyplot.ylabel('Probabilities', fontsize='x-large')

        for i in range(len(b)):
            print("For R.V. {}, the probability is {}".format(i, b[i]))
        
        pyplot.show()


    prob, trials, start, stop = parameters()
    b = binomial(prob, trials, start, stop)
    histogram(trials, b)


if __name__ == "__main__":
    main()

