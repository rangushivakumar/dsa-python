# mystr = input()
# print(mystr)
# # print(mystr.count('a',0,5))
# print(mystr.split('a'))

# print(ord('9'))


# mystr = "shivaASkumar"
# sortedstr = ""

# for i in range(len(mystr)):
#     if ord(mystr[i]) > 90:
#         sortedstr += mystr[i]
#     else:
#         distantlength = ord('A') - ord(mystr[i])
#         newchar = chr(ord('a') + (-distantlength))
#         sortedstr += newchar
# print(sortedstr)


# checking palindrome

mystr = input("Enter a string: ")
ispalindrome = True

for i in range(len(mystr)//2):
    if mystr[i] != mystr[len(mystr)-i-1]:
        ispalindrome = False
        break
    
if ispalindrome:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
