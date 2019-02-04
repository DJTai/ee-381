#!/usr/bin/env

from matplotlib import pyplot

# Prompt user for values
#   Option 1: Append values to a second list; combine two lists into one later
#   Option 2: Append both values as a tuple to a new list

x = ['Rent', 'Credit Cards', 'Food', 'Utilities', 'Transportation']
y = [2000, 400, 800, 200, 350]

xy = [(k, v) for k,v in zip(x, y)]

print(xy)
xy.sort(key=lambda x: x[1], reverse=True)   # Sort from highest value to lowest
print(xy)

pyplot.title("Household Expenses")
pyplot.xlabel("Expenses")
pyplot.ylabel("Money Spent Per Month")

x = []
y = []
for i in range(len(xy)):
    x.append(xy[i][0])
for i in range(len(xy)):
    y.append(xy[i][1])

print(x)
print(y)

# pyplot.bar(x, y)
# pyplot.show()