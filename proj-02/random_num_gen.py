#!/usr/bin/env

'''
Random Number Generator
S_i+1 = (M * S_i + A) mod N

Program used to solve Exercises 1 and 2
'''


def gen_random(s: int, n: int):
    M = 6
    A = 3
    N = 7
    i = n
    s_new = s

    while i > 0:
        print("({} * {} + {}) % {} = ".format(M, s_new, A, N), end="")
        s_new = (M * s_new + A) % N
        print(s_new)
        i -= 1
    return


def main():
    print("Seed 0:")
    gen_random(0, 10)
    print("Seed 1:")
    gen_random(1, 10)
    print("Seed 4:")
    gen_random(4, 10)
    print("Seed 5:")
    gen_random(5, 10)


if __name__ == "__main__":
    main()