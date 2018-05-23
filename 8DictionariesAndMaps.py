n = int(input())
dictionary = {}
for x in range(n):
    inside = input()
    key, value = inside.split(' ')
    dictionary[key] = value
while True:
    try:
        fromUser = input()
        if fromUser in dictionary:
            print ("%s = %s" % (fromUser, dictionary.get(fromUser)))
        else:
            print('Not found')
    except:
        break
