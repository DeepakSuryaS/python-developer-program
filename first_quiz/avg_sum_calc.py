total = 0
avg = 0
n = int(input())

for i in range(0, n+1):
    total += i

avg = total // n
print("Sum is:", total)
print("Avg is:", avg)
