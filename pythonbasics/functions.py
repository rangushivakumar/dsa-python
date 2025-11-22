# def shiva():
#     print('hello world')

# shiva()


# def sum(*number):   
#     print(number)
#     print(type(number))
#     for i in number:
#         print(i)

# sum(1,2,3)

# using * in the function arguments we can pass dynamic values to the method

#Recursion

# def rec(a):
#     a += 1
#     print('recursion stareted',a)
#     if a < 5:
#         print('recursion first step',a)
#         rec(a)

# rec(2)


# printing factorial of n

def recursion(val):
    if val == 0 or val == 1:
        return 1
    return val * recursion(val-1)

recursionanswer = recursion(5)
print(recursionanswer)
    