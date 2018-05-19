n = int(input())
for x in range(n):
    word = input()
    even = []
    odd = []
    counter = 0
    for y in word:
        if counter % 2 == 0:
            even.append(y)
        else:
            odd.append(y)
        counter = counter + 1
    print("".join(even) + " " + "".join(odd))