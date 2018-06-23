T = int(input())
for x in range(T):
    Prime = True
    number = int(input())
    if number < 2:
        print ('Not prime')
        Prime = False
    elif number == 2:
        Prime = True
    elif number % 2 == 0:
        print ('Not prime')
        Prime = False
    else:
        for y in range(3, number, 2):
            if y * y > number:
                break
            if number % y == 0:
                print ('Not prime')
                Prime = False
                break

    if Prime:
        print ('Prime')
