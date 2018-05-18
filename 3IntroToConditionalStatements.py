n = int(input())

if n % 2 == 1 or n == 2:
    print("Weird")
elif 1 < n < 6:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
elif n > 20:
    print("Not Weird")