a = int(input("Enter First numuber:"))
b = int(input("Enter Second number:"))
maxi = max(a,b)
multi = a*b
for i in range(multi+1):
    if i%a ==0 and i%b==0:
        print(i)
        break