class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)



class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        calc = 0
        for x in scores:
            calc = calc + x
        if len(scores) > 0:
            calc = calc / len(scores)
        else:
            return 'T'
        if 100 >= calc >= 90:
            return 'O'
        if 90 > calc >= 80:
            return 'E'
        if 80 > calc >= 70:
            return 'A'
        if 70 > calc >= 55:
            return 'P'
        if 55 > calc >= 40:
            return 'D'
        if 40 > calc:
            return 'T'

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
