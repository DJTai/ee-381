#!/usr/bin/env

'''
Name: David Taitingfong
ID #: 016695521
EE 381 Spring 2019
Project 01
Start Date: 01-23-2019
End Date:   02-06-2019
'''

from math import sqrt
from collections import Counter
from matplotlib import pyplot


def main():

    # initialize data
    L: list = []            # data
    N: int = 0              # for length of L
    mean: float = 0.0
    variance: float = 0.0

    L = get_integers(L)     # Get integers & print to screen
    N = len(L)              # Number of integers in the list
    mean = get_mean(L, N)   # Store mean for getting the variance
    get_median(L, N)
    get_mode(L)
    get_range(L)
    variance = get_variance(L, mean, N)
    get_std_dev(variance)

    print()
    create_pareto_chart()


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
            print('Input halted.\n')
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
    if N % 2 == 0:  # Even
        median = (L[N//2] + L[(N//2) - 1]) / 2
    else:   # Odd
        median = L[N//2]
    print('The median of the numbers entered is {}'.format(median))


def get_mode(L: list):
    """Retrieve the mode of the supplied list"""

    f_mode: list = []
    ref: int = 1     # Start reference at 1 since every number appears at least once

    c = Counter(L)
    freq = c.most_common()

    for num, val in freq:
        if val > ref:
            ref = val
            if len(f_mode) != 0:
                f_mode = []
            f_mode.append(num)
        elif val == ref:
            f_mode.append(num)

    print('The mode(s) is/are: {}'.format('None' if len(f_mode) ==
                                          0 else ", ".join(str(val) for val in f_mode)), end=" ")
    print('with frequency {}'.format(ref))

    return f_mode


def get_range(r_list: list):
    """Calculate and return the range"""

    highest = max(r_list)
    lowest = min(r_list)
    r = highest - lowest
    print("The range is {}".format(r))


def get_variance(L: list, mean: float, N: int) -> float:
    """Calculate, print, and return the variance of the supplied list"""

    top_sum = 0
    f_variance = 0.0

    for val in L:
        top_sum += (val - mean)**2
    f_variance = top_sum / N

    print('The variance is {:.3f}'.format(f_variance))

    return f_variance


def get_std_dev(list_variance):
    """Print the standard deviation to the screen"""
    print('The standard deviation is: {:.3f}.'.format(sqrt(list_variance)))


def create_pareto_chart():
    """Create pareto chart from user supplied values"""
    
    x = ['Rent', 'Credit Cards', 'Food', 'Utilities', 'Transportation']  # Bills
    y = [0 for i in range(len(x))]  # Initialize 0's for each bill

    for i in range(len(x)):
        print("The debt is {}".format(x[i]))
        y[i] = float((input("Enter the amount of money: ")))

    xy = [(k, v) for k, v in zip(x, y)]
    # Sort from highest value to lowest
    xy.sort(key=lambda x: x[1], reverse=True)

    pyplot.title("Household Expenses")
    pyplot.xlabel("Expenses")
    pyplot.ylabel("Money Spent Per Month")

    x, y = [], []
    for i in range(len(xy)):
        x.append(xy[i][0])
        y.append(xy[i][1])

    pyplot.bar(x, y, 1.0)
    pyplot.show()


if __name__ == "__main__":
    main()
