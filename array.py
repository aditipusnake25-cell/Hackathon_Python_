#========36th QUESTION========================
# arr = list(map(int,input().split()))
# total = 0
# avg = 0
# for i in range(len(arr)):
#     total = total + arr[i]
# avg = total / len(arr)
# print("Total: " , total)
# print("Average: " , avg)


#==========37th=================
# arr = list(map(int,input().split()))
# maxi = arr[0]
# mini = arr[0]
# for x in range(len(arr)):
#     if arr[x]>maxi:
#         maxi = arr[x]
#     if arr[x]<mini:
#         mini = arr[x]
# print(maxi)
# print(mini)

#================38th===============
# arr = list(map(int,input().split()))
# maxi = arr[0]
# second = arr[0]
# for x in range(len(arr)-1):
#     if arr[x]>maxi:
#         maxi = arr[x]
#         arr.remove(maxi)
#     if arr[x]>second:
#         second = arr[x]
#     if second < maxi:
#         second = second 
#     else:
#         second = maxi
# print(second)
    
#========39============

# arr = list(map(int,input().split()))
# odd = 0
# even = 0
# for x in range(len(arr)):
#     if arr[x]%2==0:
#         even = even+1
#     else:
#         odd = odd+1
# print("Even: " , even)
# print("Odd: " , odd)

#=======40============

# arr = list(map(int,input().split()))
# zero = 0
# neg = 0
# pos = 0
# for i in range(len(arr)):
#     if arr[i]>0:
#         pos = pos+1
#     elif arr[i]<0:
#         neg = neg +1
#     else:
#         zero =zero+1
# print("Positive:" , pos , "Negative:" , neg , "Zero:" , zero)

#======41th=============
# arr = list(map(int,input().split()))
# a = len(arr)-1
# arri=[]
# while a>=0:
#     arri.append(arr[a])
#     a=a-1
# for num in arri:
#     print(num , end=" ")

#===========42th==========

# arr = list(map(int,input().split()))
# array = []
# for i in arr:
#     array.append(i)
# print(array)

 
#=========43th==============

# arr = list(map(int,input().split()))
# k = int(input("Enter targeted index:"))
# x = int(input("Enter number to add:"))
# arri = []
# for i in range(len(arr)):
#     if i==k:
#         arri.append(x)
#         arri.append(arr[i])
#     else:
#         arri.append(arr[i])
# print(arri)

#=====44th============

# arr = list(map(int,input().split()))
# k = int(input("Enter targeted index:"))
# arri=[]
# for i in range(len(arr)):
#     if i == k:
#         continue
#     else:
#         arri.append(arr[i])
# print(arri)

#=========45th==========

# arr = list(map(int,input().split()))
# k = int(input("Enter targeted index:"))
# arr1=[]
# arr2=[]
# arr3=[]
# for i in range(len(arr)):
#     if i == k:
#         break
#     elif i>k:
#         arr1.append(arr[i])
#     else:
#         arr2.append(arr[i])
# arr3.append(arr2)
# arr3.append(arr1)
# print(arr3)

