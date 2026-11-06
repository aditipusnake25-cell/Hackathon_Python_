n = int(input())
temp = n
count = 0
total = 0
while temp > 0:
    digit = temp % 10
    count = count + 1
    temp = temp // 10
temp = n
while temp > 0:
    digit = temp % 10
    total = total + (digit ** count)
    temp = temp // 10
if n == total:
    print("Armstrong")
else:
    print("Not Armstrong")