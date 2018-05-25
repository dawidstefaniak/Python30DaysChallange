#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binaryrep = "{0:b}".format(n)
    counter = 0
    forcounter = 0
    for x in binaryrep:
        if x == "1":
            forcounter += 1
        else:
            if forcounter > counter:
                counter = forcounter
            forcounter = 0
    if forcounter > counter:
        counter = forcounter
    print(counter)

