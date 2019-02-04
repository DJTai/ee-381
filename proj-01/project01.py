#!/usr/bin/env

# EE 381 Spring 2019 Project 01
# David Taitingfong
# 016695521
# Start  Date: 01-23-2019
# End Date:    01-??-2019
# ------------------------------------
# This project does summary statistics
# and a Pareto chart
# ------------------------------------

from math import sqrt
from collections import Counter
from matplotlib import pyplot


def main():

    # initialize data
    L: list = []            # data
    N: int = 0              # for length of L
    range: int = 0
    mean: float = 0.0
    variance: float = 0.0

    L = get_integers(L)
    N = len(L)              # Number of integers in the list
    mean = get_mean(L, N)   # Store mean for getting the variance
    get_median(L, N)
    get_mode(L)

    range = L[N - 1] - L[0]
    print('The range of the list: {}'.format(range))

    variance = get_variance(L, mean, N)
    print('The standard deviation is: {:.3f}.'.format(sqrt(variance)))

    # Pareto chart created w/ household spending data given
    # TODO: Change to actual data
    x = [0, 1, 2, 3]
    y = [5, 2, 4, 1]
    pyplot.plot(x, y)
    pyplot.show()


def get_integers(f_L: list) -> list:
    """Retrieves a list of integers from the user"""

    v = 1   # Initial value for boolean variable

    print('You will be asked to input non-negative integers.')
    print('When you are done, enter a letter to stop.')

    while v == 1:
        try:
            l = int(input('Enter a non-negative integer: '))
            if (l < 0):
                print(
                    '\nERROR: That number is negative. Please enter a non-negative integer\n')
            else:
                f_L.append(l)
        except ValueError:
            print('Input halted.')
            print('\n')
            v = 0

    print('You inputted the following list of numbers: ', f_L)
    print('\n')

    return f_L


def get_mean(L: list, N: int) -> float:
    """Calculate and retrieve the mean of the list"""

    s = sum(L)  # The sum of the inputted numbes
    N = len(L)
    f_mean = s / N
    print('The mean of the numbers entered is {:.3f}'.format(f_mean))

    return f_mean


def get_median(L, N):
    """Print the median of the supplied list"""

    L.sort()  # Sort the list
    median = 0

    # It is necessary to determine whether or not the length of the list is even
    # or odd
    if N % 2 == 0:
        # Even
        median = (L[N//2] + L[(N//2) - 1]) / 2
    else:
        # Odd
        median = L[N//2]
    print('The median of the numbers entered is {}'.format(median))


def get_mode(L: list):
    """Retrieve the mode of the supplied list"""

    mode: list = []
    ref: int = 1     # Start reference at 1 since every number appears at least once

    c = Counter(L)
    freq = c.most_common()

    for num, val in freq:
        if val > ref:
            ref = val
            if len(mode) != 0:
                mode = []
            mode.append(num)
        elif val == ref:
            mode.append(num)

    print('The mode(s) is/are: {}'.format('None' if len(mode) ==
                                          s0 else ", ".join(str(val) for val in mode)), end=" ")
    print('with frequency {}'.format(ref))

    return mode


def get_variance(L: list, mean: float, N: int) -> float:
    """Calculate and retrieve the variance of the supplied list"""

    top_sum = 0
    f_variance = 0

    for val in L:
        top_sum += (val - mean)**2
    f_variance = top_sum / N

    print('The variance is {:.3f}'.format(f_variance))

    return f_variance


if __name__ == "__main__":
    main()
