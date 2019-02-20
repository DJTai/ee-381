#!/usr/bin/env

from matplotlib import pyplot

x = ['Rent', 'Credit Cards', 'Food', 'Utilities', 'Transportation'] # Bills
y = [0 for i in range(len(x))]  # Initialize 0's for each bill

for i in range(len(x)):
    print("The debt is {}".format(x[i]))
    y[i] = float((input("Enter the amount of money: ")))

xy = [(k, v) for k,v in zip(x, y)]
xy.sort(key=lambda x: x[1], reverse=True)   # Sort from highest value to lowest

pyplot.title("Household Expenses")
pyplot.xlabel("Expenses")
pyplot.ylabel("Money Spent Per Month")

x, y = [], []
for i in range(len(xy)):
    x.append(xy[i][0])
    y.append(xy[i][1])

pyplot.bar(x, y, 1.0)
pyplot.show()