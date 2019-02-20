#!/usr/bin/env

'''
Name: David Taitingfong
ID #: 016695521
EE 381 Spring 2019
Project 02
Start Date: 02-11-2019
End Date:   02-20-2019
'''

import time
import math


def flip_a_coin(n: int) -> None:
    """Simulates flipping a coin `n` number of times"""

    M = 8601                # Multiplier
    A = 4857                # Adder
    N = 10000               # Norm
    S = time.process_time()  # Seed
    heads, tails, total = 0, 0, 0   # Counters

    while n != 0:
        n -= 1
        S = (S * M + A) % N
        r = S / N
        coin = math.floor(2*r)
        if coin == 0:
            tails += 1
        else:
            heads += 1
        total += 1

    print("\tHeads appeared {} times".format(heads))
    print("\tTails appeared {} times\n".format(tails))
    return


def roll_die(n: int) -> None:
    """Simulates rolling a die `n` times"""

    M = 8601                # Multiplier
    A = 4857                # Adder
    N = 10000               # Norm
    S = time.process_time()  # Seed
    s1, s2, s3, s4, s5, s6 = 0, 0, 0, 0, 0, 0   # Die sidess

    while n != 0:
        n -= 1
        S = (S * M + A) % N
        r = S / N
        side = math.floor(6*r)  # Get a side
        if side == 1:
            s1 += 1
        elif side == 2:
            s2 += 1
        elif side == 3:
            s3 += 1
        elif side == 4:
            s4 += 1
        elif side == 5:
            s5 += 1
        else:
            s6 += 1

    print("\t1 appeard {} times".format(s1))
    print("\t2 appeard {} times".format(s2))
    print("\t3 appeard {} times".format(s3))
    print("\t4 appeard {} times".format(s4))
    print("\t5 appeard {} times".format(s5))
    print("\t6 appeard {} times\n".format(s6))
    return


def probability_problem(n: int) -> None:
    """Simulates tossing 3 balls randomly into 5 cans an `n` number of times"""

    M = 8601                # Multiplier
    A = 4857                # Adder
    N = 1000                # Norm
    S = time.process_time()  # Seed
    ball = [0, 0, 0]        # Initially no balls in any cans
    ctr = 0
    trials = n

    while n != 0:
        for i in range(len(ball)):
            S = (S * M + A) % N
            r = S / N
            can_num = math.floor(r * 5 + 1)  # Get a can number
            ball[i] = can_num

        if ball[0] != ball[1] and ball[1] != ball[2] and ball[0] != ball[2]:
            ctr += 1
        n -= 1

    print("\tThe probability of the three balls being in different cans is {0:.4f}\n".format(
        ctr/trials))
    return


def main():
    print("Flipping a coin 25 times:")
    flip_a_coin(25)

    print("Rolling a die 25 times:")
    roll_die(25)

    print("Probabilty problem with 1,008,001 trials")
    probability_problem(1008001)
    return


if __name__ == "__main__":
    main()
