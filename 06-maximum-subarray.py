"""
Find the largest sum of a contiguous subarray (containing at least one number)
within an array.

For example, given the array [-2, 1, -3, 4, -1, 2, 1, -5, 4], the contiguous
subarray [4, -1, 2, 1] has the largest sum of 6.

Problem provided by: https://leetcode.com/problems/maximum-subarray/
"""

def maximum_subarray_brute_force(nums):
  if len(nums) == 0:
    return 0
  max_sum = nums[0]
  for i in range(len(nums)):
    for j in range(i + 1, len(nums) + 1):
      max_sum = max(max_sum, sum(nums[i:j]))
  return max_sum

def maximum_subarray(nums):
  if len(nums) == 0:
    return 0
  max_sum = nums[0]
  curr_sum = nums[0]
  for num in nums[1:]:
    curr_sum = max(curr_sum + num, num)
    max_sum = max(max_sum, curr_sum)
  return max_sum

print(maximum_subarray_brute_force([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
print(maximum_subarray_brute_force([]) == 0)
print(maximum_subarray_brute_force([1]) == 1)
print(maximum_subarray_brute_force([-2, -1]) == -1)

print(maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
print(maximum_subarray([]) == 0)
print(maximum_subarray([1]) == 1)
print(maximum_subarray([-2, -1]) == -1)
