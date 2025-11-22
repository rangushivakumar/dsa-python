# for i in range(10):
#     print(i)

# i = 0
# while i < 5:
#     if i%2 == 0: 
#         print("0", end='')
#     else:
#         print('*', end='')
#     i += 1


# i = 0
# while i < 5:
#     i += 1
#     if i%2 == 0:
#         continue
#     print(f'odd numbers: {i}')


# 1,2,4,8,16,32,64


# Pattern printing


# row = int(input())
# col = int(input())

# for i in range(row):
#     for j in range(col):
#         print(j+1,end=' ')
#     print('')

# a = int(input())

# for i in range(1,a+1):
#     for j in range(i):
#         print(j+1, end=' ')
#     print('')  


a = int(input())


for row in range(1,a+1):
    for col in range(a,0,-1):
        if col > row:
            print(' ', end='')
        else:
            print('*', end='')
    print('')