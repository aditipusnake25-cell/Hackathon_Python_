# # seats = input().split()
# # row_a=0
# # total=0
# # let="A"
# # for i in range(len(seats)):
# #     for x in range(i):
# #         total+=i[x+1 :]
# #         print(i[x]," -> ",i[x+1 :])
# #     if let in seats[i]:
# #         row_a+=1
# # print(row_a , total)

# # passwords=input().split()
# # # num=1234567890
# # strong=0
# # for password in passwords:
# #     length=len(password)
# #     deg=0
# #     for char in password:
# #         if char in "1234567890":
# #             deg=deg+1
# #     if length>=6 and deg>0:
# #         strong+=1
# #         print("Strong")
# #     else:
# #         print("Weak")
# # print("Strong Passwords : ",strong)


# # distances=list(map(int,input().split()))
# # total_d=0
# # count=1
# # longest_d=distances[0]
# # distance=100
# # for x in range(len(distances)):
# #     distance=distance-distances[x]*2
# #     if distance>20:
# #         print("Checkpoint ",count,": ",distance)
# #         count+=1
# #     else:
# #         print("Checkpoint ",count,": ",distance)
# #         print("Energy Critical")
# #         count+=1
# #     total_d+=distances[x]
# #     if distances[x]>longest_d:
# #         longest_d=distances[x]
# #         location = x+1
# # print("Total Distance: ",total_d,"km")
# # print("Longest Distance: ",longest_d,"km")
# # print("Longest Distance at checkpoint: ",location)
# # print("Final Energy: ",distance)

# # boys = input().split()
# # girls=input().split()
# # arr=[]
# # for i in range(len(boys)):
# #         arr.append(boys[i])
# #         arr.append(girls[i])
# # print(arr)
# # print("Total names: ", len(arr))

# # word = input()
# # Con=0
# # Vow=0
# # for ch in word:
# #     total=0
# #     vowel = 0
# #     consonant = 0
# #     if ch in "aeiou":
# #         vowel+=2
# #         Vow+=2
# #         print(ch, "->" , vowel)
# #     else:
# #         consonant+=1
# #         Con+=1
# #         print(ch , "->", consonant)
# #     total=Vow+Con
# # print(total)'


# # temp=list(map(int,input().split()))
# # difference=0
# # for i in range(len(temp)-1):
# #     var=i+1
# #     if temp[i]<temp[var]:
# #         difference=temp[var]-temp[i]
# #         print("Increased by ",difference)
# #     elif temp[i]>temp[var]:
# #         difference=temp[i]-temp[var]
# #         print("Decreased by ",difference)
# #     else:
# #         print("No Change")

# # n=int(input())
# # for i in range(1,n+1):
# #     if i%2!=0:
# #         print("1 2 3 4 5")
# #     else:
# #         print("5 4 3 2 1")


# # amount=int(input("Enter Amount.."))
# # if amount>=10000:
# #     discount = amount*15/100
# #     final=amount-discount
# #     print(final)
# # elif amount>=5000 and amount<=9999:
# #     discount=amount*10/100
# #     final = amount-discount
# #     print(final)
# # elif amount>=1000 and amount<=4999:
# #     discount=amount*5/100
# #     final = amount-discount
# #     print(final)
# # else:
# #     print(amount)



# n = input()

# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
# count = 0
# for i in range(len(n)):
#     if n[i] == "I":
#         if i + 1 < len(n) and (n[i+1] == "V" or n[i+1] == "X"):
#             count -= I
#         else:
#             count += I
#     elif n[i] == "V":
#         count += V
#     elif n[i] == "X":
#         if i + 1 < len(n) and (n[i+1] == "L" or n[i+1] == "C"):
#             count -= X
#         else:
#             count += X
#     elif n[i] == "L":
#         count += L
#     elif n[i] == "C":
#         if i + 1 < len(n) and (n[i+1] == "D" or n[i+1] == "M"):
#             count -= C
#         else:
#             count += C
#     elif n[i] == "D":
#         count += D
#     else:
#         count += M
# print(count)


# arr=list(map(int,input().split()))
# num = (len(arr)-1)
# array=[]
# array2=[]
# for i in range(len(arr)):
#     if arr[i]!=num:
#         array.append(num)
#     if arr[i]==num:
#         array.append(num)
#     if array[i]>9:
#         ch=array.split()
#         array2.append(ch)
# print(array)
# print(arr)

# name = input()
# i = len(name)-1
# reverse=""
# while i>=0:
#     reverse=reverse+name[i]
#     i=i-1
# print(reverse)



# name = input()
# i = len(name)-1
# reverse=""
# while i>=0:
#     reverse=reverse+name[i]
#     i=i-1
# if reverse == name:
#     print("True")
# else:
#     print("False")

# name = input("Enter a string: ")

# i = 0

# while i < len(name):
#     count = 0 
#     j = 0

#     while j < len(name):
#         if name[i] == name[j]:
#             count += 1
#         j += 1

#     if count == 1:
#         print(name[i])
#         break

#     i += 1

# if i == len(name):
#     print(-1)


# arr = list(map(int,input().split()))
# lar = arr[0]
# sec = arr[0]
# for i in range(len(arr)):
#     if arr[i]>lar:
#         lar = arr[i]
# for x in range(len(arr)):
#     if arr[x]==lar:
#         continue
#     elif arr[x]>sec:
#         sec=arr[x]
# if lar>sec:
#     print(sec)
# else:
#     print(lar)

# n = int(input())
# addi =0
# num=0
# while n>0:
#     num = n%10
#     addi = addi+num
#     n = n//10
# print(addi)


# n =input()
# vov = 0
# conso = 0
# for ch in n:
#     if ch in "aeiou":
#         vov = vov+1
#     else:
#         conso = conso+1
# print("Vowel: ",vov , "Consonant: ",conso)

# n = input()
# m = input()
# st1 = n.sort()
# st2 =m.sort()
# if st1 ==st2:
#     print("both Anagram")
# else:
#     print("Not")

# n = input()
# largest = 0
# count = 0
# for i n range(len(n)):
#     if n[i]==n[i+1]:
#         count+=1
    
# string1=input()
# string2=input()
# count = 0
# for ch in string1:
#     if ch in string2:
#         count=count+1
# if count == len(string1) or count == len(string2):
#     print("True")
# else:
#     print("False")

string = input()
copy = ""
for ch in string:
    if ch in copy :
        continue 
    else:
        copy = copy+ch
print(len(copy))