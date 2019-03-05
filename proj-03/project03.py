#!/usr/bin/env

'''
Name: David Taitingfong
ID #: 016695521
EE 381 Spring 2019
Project 03
Start Date: 02-27-2019
End Date:   03-03-2019
'''

import random


def part_01():
    """Part 1 of Project 3 - Bernoulli R.V."""

    print("Simulation of Bernoulli RV")
    p = float(input("Enter the probability of success: "))
    T = int(input("How many trials? "))

    for i in range(T):
        r = random.uniform(0, 1)
        print("1", end=" ") if r < p else print("0", end=" ")
        if (i + 1) % 5 == 0:
            print()

    print('\n')

    return


def part_02():
    """Part 2 of Project 3 - Discrete Markov Chain"""

    print("Discrete Markov Chain")
    L = []  # For recording particle positions
    S = random.randint(0, 1)
    L.append(S)  # Initial position in list

    p = float(input("Enter the probability of going from 0 to 1: "))
    q = float(input("Enter the probability of going from 1 to 0: "))

    for i in range(25):
        r = random.uniform(0, 1)
        if S == 0 and r < p:
            S = 1
        elif S == 1 and r < q:
            S = 0
        L.append(S)

    for i in range(len(L) - 1):
        print("{} ".format(L[i]), end=" ")
        if (i + 1) % 5 == 0:
            print()

    print('\n')

    return


def main():
    # part_01()
    part_02()


if __name__ == "__main__":
    main()
