#!/bin/python3

import math
import os
import random
import re
import sys


class database:
    def __init__(self):
        self.name = []
        self.email = []
        self.id = []
        self.counter = 0

    def addValues(self, name, email):
        self.name.append(name)
        self.email.append(email)
        self.id.append(self.counter)
        self.counter += 1

    def getNames(self):
        i = 0
        for x in self.email:
            toprint = re.match(".*@gmail\.com", x)
            if toprint:
                print(self.name[i])
            i += 1


if __name__ == '__main__':
    N = int(input())
    db = database()
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        db.addValues(firstName, emailID)

    db.getNames()
