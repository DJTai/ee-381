#!/usr/bin/env

def main(): 
    L = []  # Empty list for data
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
    # ---------------------------------------------------------

    # Calculation of the mean
    s = sum(L)  # The sum of the inputted numbes
    N = len(L)
    mean = s / N
    print('The mean of the numbers entered is {}'.format(mean))
    # ---------------------------------------------------------

    # Calculation of the median
    L.sort()  # Sort the list
    # It is necessary to determine whether or not the length of the list is even
    # or odd
    if N % 2 == 0:
        # Even
        median = (L[N//2] + L[(N//2) - 1]) / 2
    else:
        # Odd
        median = L[N//2]
    print('The median of the numbers entered is {}'.format(median))

if __name__ == "__main__":
    main()