import datetime

returnstring = input().split(' ')
expectedstring = input().split(' ')
returndate = datetime.datetime(int(returnstring[2]), int(returnstring[1]), int(returnstring[0]))
expectdate = datetime.datetime(int(expectedstring[2]), int(expectedstring[1]), int(expectedstring[0]))
difference = returndate - expectdate
if difference.days < 0:
    print(0)
elif difference.days < 31 and expectdate.month == returndate.month:
    print(str(15*difference.days))
elif expectdate.month != returndate.month and expectdate.year == returndate.year:
    print(str((returndate.month - expectdate.month)*500))
elif expectdate.year < returndate.year:
    print(10000)

