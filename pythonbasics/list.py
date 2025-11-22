# create a list of 5 numbers and print it
# numberslist = []
# len = int(input())
# for i in range(1, len+1):
#     numberslist.append(i)

# print(numberslist)


# access elements using both positive indexing and negative indexing
# fruits = ['apple','banana','mango','orange']
# for i in range(-1,-(len(fruits)+1),-1):
#     print(fruits[i])


# modify the 3rd element of the list
# fruits = ['a','b','c']
# fruits[2] = 'd'
# print(fruits)


# add an element to the list 
# number = [1,2,3,4]
# number.append(5)
# print(number)

# remove and del element

# number.remove(1)
# print(number)
# del(number[0])
# print(number)
# print(len(number))

# print(sum(number))

# print sum of number of the list
# numberlist = [1,2,3,4,5]
# a = 0
# for i in range(len(numberlist)):
#     a = a + numberlist[i]
#     if i == (len(numberlist)-1):
#         print(a)

# find max or min element

# numbers = [4, 7, 2, 9, 5]
# print(max(numbers))
# print(min(numbers))
# max = 0
# for i in range(len(numbers)):
#     if i == 0:
#         max = numbers[i]
#     elif numbers[i] > max:
#         max = numbers[i]

# print(max)


# count even and odd numbers in the list
# numbers = [4, 7, 2, 9, 5]
# odd = 0
# even = 0
# for i in range(len(numbers)):
#     if numbers[i]%2 == 0:
#         even = even + 1
#     else:
#         odd += 1

# print(even)
# print(odd)


# reverse a list using loop or slicing

# numbers = [4, 7, 2, 9, 5]
# reversedlist = []
# for i in range(-1,-(len(numbers)+1),-1):
#     reversedlist.append(numbers[i])
# print(reversedlist)

# usingslicelist = numbers[::-1]
# print(usingslicelist)


# mylist = input('enter numbers sepreated by space ').split()
# numlist = []
# for item in mylist:
#     numlist.append(int(item))

# print(numlist)
# print(type(numlist[0]))
    

# list comprehension
# List comprehension is a concise and elegant way to create lists in Python.
# It allows you to generate a new list by applying an expression to each element of an iterable (like a list, tuple, or range), all in a single line of code.
    
# syntax
# [expression for item in iterable if condition]

# mylist = [item*2 for item in range(6) if item%2 == 0]
# print(mylist)
# mylist2 = [item for item in input().split()]
# print(mylist2)

# mylist3 = [int(item) for item in input().split()]
# print(mylist3)


# remove duplicates from a list
# mylist = [int(item) for item in input("Enter numbers: ").split()]
# cleanlist = []

# for item in mylist:
#     exists = 0  
#     for x in cleanlist:
#         if x == item:
#             exists = 1
#             break

#     if exists == 0:
#         cleanlist.append(item)

# print("Original list:", mylist)
# print("List without duplicates:", cleanlist)


# rows = int(input())
# colms = int(input())

# matrix = []

# for i in range(rows):
#     rows = []
#     for j in range(colms):
#         rows.append(int(input(f"Enter element [{i}][{j}]: ")))
#     matrix.append(rows)

# print(matrix)

# rows = int(input())

# matrix = []

# for i in range(rows):
#     templist = [int(item) for item in input().split()]
#     matrix.append(templist)

# print(matrix)


# trace of a matrix
# sum = 0
# tracematrix = []
# for i in range(rows):
#     sum = sum + matrix[i][i]
#     tracematrix.append(matrix[i][i])

# print(sum,tracematrix)

# Transpose of a square matrix
# for i in range(rows):
#     for j in range(i + 1, rows):
#         temp = matrix[i][j]
#         matrix[i][j] = matrix[j][i]
#         matrix[j][i] = temp

# print(matrix)








            




