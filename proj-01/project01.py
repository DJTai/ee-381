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
import math

def main():
    L: list = []  # Empty list for data
    N: int = 0
    range: int = 0
    mean: float = 0.0
    variance: float = 0.0

    get_integers(L)

    N = len(L)  # Number of integers in the list

    mean = get_mean(L, N)
    get_median(L, N)
    get_mode(L)

    # Range - Hi vs lo
    range = L[N - 1] - L[0]
    print('The range of the list: {}'.format(range))

    # Variance
    variance = get_variance(L, mean, N)
    
    # Standard Deviation
    print('The standard deviation is: {:.3f}.'.format(math.sqrt(variance)))

    # Pareto chart created w/ household spending data given

def get_integers(L: list):
    v = 1   # Initial value for boolean variable

    print('You will be asked to input non-negative integers.')
    print('When you are done, enter a letter to stop.')

    while v == 1:
        try:
            l = int(input('Enter a non-negative integer: '))
            if (l < 0):
                print('\nERROR: That number is negative. Please enter a non-negative integer\n')
            else:
                L.append(l)
        except ValueError:
            print('Input halted.')
            print('\n')
            v = 0

    print('You inputted the following list of numbers: ', L)
    print('\n')

def get_mean(L: list, N: int) -> float:
    # Calculation of the mean
    s = sum(L)  # The sum of the inputted numbes
    N = len(L)
    f_mean = s / N
    print('The mean of the numbers entered is {:.3f}'.format(f_mean))
    
    return f_mean
    # ---------------------------------------------------------

def get_median(L, N):
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
    mode:int = 0

    return mode

def get_variance(L: list, mean: float, N: int) -> float:
    top_sum = 0
    f_variance = 0

    for val in L:
        top_sum += (val - mean)**2

    f_variance = top_sum / N

    print('The variance is {:.3f}'.format(f_variance))
    return f_variance


if __name__ == "__main__":
    main()