class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        array = []
        for x in range(1,(n + 1)):
            if n % x == 0:
                array.append(x)
        sum = 0
        for num in range(len(array)):
            sum = sum + array[num]
        return sum


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)