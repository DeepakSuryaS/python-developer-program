n = int(input())
factorial = n

if(n == 1):
    print("Factorial is 1.")
elif(n == 0):
    print("Factorial is 1.")
else:
    while n > 1:
        factorial = factorial * (n - 1)
        n = n - 1
    print("Factorial is",factorial)

