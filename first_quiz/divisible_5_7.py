by7 = []
by5 = []
for num in range(1500, 2701):
    if(num % 7 == 0):
        by7.append(num)
    if(num % 5 == 0):
        by5.append(num)

print(by7, "are the numbers divisible by 7.")
print(by5, "are the numbers divisible by 5.")
