#!/bin/python3
#https://www.hackerrank.com/challenges/a-very-big-sum/problem

import os
import sys

def aVeryBigSum(n, ar):
    res = 0
    for x in range(n):
        res = res + ar[x]
    return res

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(n, ar)

    f.write(str(result) + '\n')

    f.close()
