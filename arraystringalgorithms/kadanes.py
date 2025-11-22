# nums = [-2,1,-3,4,-1,2,1,-5,4]

# def max_subarray_sum(nums):
#     currsum = 0
#     ovalsum = 0

#     curr_start = 0                  # start of current subarray
#     best_start = 0                  # start of best subarray
#     best_end = 0                    # end of best subarray

#     for i in range(len(nums)):
#         if i == 0:
#             currsum = nums[i]
#             ovalsum = nums[i]
#             curr_start = 0
#             best_start = 0
#             best_end = 0
#         else:
#             check = currsum + nums[i]

#             if check > nums[i]:
#                 currsum = check
#             else:
#                 currsum = nums[i]
#                 curr_start = i      # restarting subarray

#             if currsum > ovalsum:
#                 ovalsum = currsum
#                 best_start = curr_start
#                 best_end = i

#     # print the best subarray
#     for i in range(best_start, best_end + 1):
#         print(nums[i], end=" ")

#     print("\noverallsum is:")
#     return ovalsum


# print(max_subarray_sum(nums))


# def maxsubarraysum(nums):
#     maxsum = nums[0]
#     currsum = nums[0]
#     for i in nums[1:]:
#         currsum = max(i, currsum + i)
#         maxsum = max(maxsum, currsum)
#     return maxsum

# print(maxsubarraysum(nums))

# 2d kadane's algorithm

# rows = int(input())

# matrix = []

# for i in range(rows):
#     templist = [int(item) for item in input().split()]
#     matrix.append(templist)

