class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
        self.counter = 0

    def maximumDifference(self):
        return self.maximumDifference

    def computeDifference(self):
        for x in range(self.counter, len(self.__elements)):
            variable = abs(abs(self.__elements[self.counter]) - abs(self.__elements[x]))
            if variable >= self.maximumDifference:
                self.maximumDifference = variable
        self.counter = self.counter + 1
        # Recursive method which will call itself
        # if there are at least 2 elements left to compare
        if self.counter != len(self.__elements):
            self.computeDifference()

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
