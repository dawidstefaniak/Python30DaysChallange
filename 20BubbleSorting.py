#!/bin/python3
import sys


class Sorting(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.swaps = 0

    def Sort(self):
        for i in range(self.x):
            for j in range(self.x - 1):
                if self.y[j] > self.y[j + 1]:
                    temp = self.y[j]
                    self.y[j] = self.y[j + 1]
                    self.y[j + 1] = temp
                    self.swaps += 1


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
sorting = Sorting(n, a)
sorting.Sort()
print("Array is sorted in " + str(sorting.swaps) + " swaps.")
print("First Element: " + str(sorting.y[0]))
print("Last Element: " + str(sorting.y[sorting.x - 1]))