# You are given an integer array nums and an integer target.
# Return the indices of the two numbers such that they add up to target.

# Conditions:

# Exactly one valid answer exists.

# You cannot use the same element twice.

# The answer can be returned in any order.

# nums = [2, 7, 11, 15]
# target = 9
# Output: [0, 1]
# Explanation: nums[0] + nums[1] = 2 + 7 = 9

# Brute Force Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# def bruteforce2sum(nums, target):
#     pairs = []
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
                # pairs.append([i, j])
#                 return [i, j]
#     return pairs
# nums = [1, 3, 2, 2, 3]
# target = 5

# index = bruteforce2sum(nums, target)
# print("Brute Force Approach:", index)  

# sorting an array 
# nums=[5,3,8,6,2]
# def sortingarray(nums):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i]>nums[j]:
#                 # nums[i], nums[j]=nums[j], nums[i]
#                 temp=nums[i]
#                 nums[i]=nums[j]
#                 nums[j]=temp
#     return nums

# print("Sorted Array:", sortingarray(nums))  # Output: [2, 3, 5, 6, 8]


# Optimized Approach using Hash Map
# def optimized2sum(nums, target):
#     nums.sort()
#     start = 0
#     end = len(nums) - 1
#     while start < end:
#         currsum = nums[start] + nums[end]
#         if currsum == target:
#             return [start, end]
#         elif currsum < target:
#             start = start + 1
#         else:
#             end = end - 1
#     return []

    
# index = optimized2sum(nums, 12)
# print("Optimized Approach:", index)


# Note: The above optimized approach will not return the original indices of the elements in the unsorted array,
# modifying the above function to return the original indices.
# use flag to donot reuse same element twice
# def two_sum_with_indices(nums, target):
#     newnums = nums.copy()
#     nums.sort()
#     start = 0
#     end = len(nums) - 1
#     while start < end:
#         currsum = nums[start] + nums[end]
#         if currsum == target:
#             ans = []
#             first_found = False
#             second_found = False
#             for i in range(len(newnums)):
#                 if newnums[i] == nums[start]:
#                     if not first_found:
#                         ans.append(i)
#                     first_found = True
#                 elif newnums[i] == nums[end]:
#                     if not second_found:
#                         ans.append(i)
#                     second_found = True
#             return ans
#         elif currsum < target:
#             start = start + 1
#         else:
#             end = end - 1
#     return []
# nums = [2, 7, 11,11, 15]
# index = two_sum_with_indices(nums, 26)
# print("Optimized Approach with Indices:", index)

#  the indices were geting changed after sorting the array.
#  To maintain the original indices, we can use a hash map to store the values and their corresponding indices before sorting.
# def optimized2sum_with_indices(nums, target):
#     num_to_index = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in num_to_index:
#             return [num_to_index[complement], i]
#         num_to_index[num] = i
#     return []


# index = optimized2sum_with_indices(nums, 9)
# print("Optimized Approach with Indices:", index)


# 3sum problem

# def three_sum(nums, target):
#     newnums = nums.copy()
#     nums.sort()
#     for i in range(len(nums)):
#         fixednum = nums[i]
#         start = i + 1
#         end = len(nums) - 1
#         while start < end:
#             currsum = fixednum + nums[start] + nums[end]
#             ans = []
#             if currsum == target:
#                 for i in range(len(newnums)):
#                     if newnums[i] == fixednum or newnums[i] == nums[start] or newnums[i] == nums[end]:
#                         ans.append(i)
#                 return ans
#             elif currsum < target:
#                 start = start + 1
#             else:
#                 end = end - 1
#     return []
# nums = [2, 7, 11, 15, -2, 4]
# index = three_sum(nums, 9) 
# print("Three Sum Indices:", index)  


# Dutch National Flag Algorithm
def dutch_national_flag(arr):
    low = 0
    mid = 0
    high = len(arr)-1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

# Example usage:
arr = [2, 0, 1, 2, 1, 0]
sorted_arr = dutch_national_flag(arr)
print("Sorted Array using Dutch National Flag Algorithm:", sorted_arr)  # Output: [0, 0, 1, 1, 2, 2]
# Time Complexity: O(n)
# Space Complexity: O(1)

# with time complexity O(2n)
def dutch_national_flag_two_pass(arr):
    count0 = 0
    count1 = 0
    count2 = 0
    
    for num in arr:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1
            
    index = 0
    for _ in range(count0):
        arr[index] = 0
        index += 1
    for _ in range(count1):
        arr[index] = 1
        index += 1
    for _ in range(count2):
        arr[index] = 2
        index += 1
        
    return arr

# Example usage:
arr = [2, 0, 1, 2, 1, 0]
sorted_arr = dutch_national_flag_two_pass(arr)
print("Sorted Array using Two-Pass Dutch National Flag Algorithm:", sorted_arr)  # Output: [0, 0, 1, 1, 2, 2]
# Time Complexity: O(2n)
# Space Complexity: O(1)