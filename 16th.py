n = int(input())
for num in range(2, n+1):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count = count + 1
    if count == 0:
        print(num, end=" ")