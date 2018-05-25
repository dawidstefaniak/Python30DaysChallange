#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    x = 0
    y = 0
    maxsum = -9999
    for x in range(4):
        for y in range(4):
            result = arr[x][y] + arr[x][y+1] + arr[x][y+2] + arr[x+1][y+1] + arr[x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]
            if result > maxsum:
                maxsum = result
    print(maxsum)
