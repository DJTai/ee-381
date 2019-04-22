#!/usr/bin/env

"""
EE 381 Project 05
Name:    David Taitingfong
I.D.:    016695521
S.Date:  04-17-2019
E.Date:  04-22-2019

Description:
    This is the power curve for project 5.
    The 1-Beta vs ~p curve

State the hypothesis:
    Ho: p = 1/2
    H1: p > 1/2

Type II or Beta Error
~p vals 
0.55        0.8926
0.60        0.7917
0.65        0.6458
0.70        0.4659
0.75        0.2817
0.80        0.1326
0.85        0.0415
0.90        0.0065
0.95        0.0002
1.00        0.0

The Power of the Test
"""

from matplotlib import pyplot


def main():
    # ~p values
    p = [0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00]
    
    # Corresponding Beta values via Project 4
    beta = [0.8926, 0.7917, 0.6458,
            0.4659, 0.2817, 0.1326,
            0.0415, 0.0075, 0.0002, 0.0]

    b = []  # Y-axis

    for val in beta:
        b.append(1 - val)

    pyplot.plot(p, b)
    pyplot.title("Power Curve")
    pyplot.xlabel("Values of p")
    pyplot.ylabel("1 - β")
    pyplot.show()
    

if __name__ == "__main__":
    main()

