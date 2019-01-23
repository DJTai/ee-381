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

L = []  # Empty list for data
v = 1   # Initial value for boolean variable

print('You will be asked to input non-negative integers.')
print('When you are done, enter a letter to stop.')

while v == 1:
    try:
        l = int(input('Enter a non-negative integer: '))
        L.append(l)
    except ValueError:
        print('Input halted.')
        print('\n')
        v = 0

print('You inputted the following list of numbers: ', L)
print('\n')