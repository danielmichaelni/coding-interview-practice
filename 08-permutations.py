"""
Given a collection of distinct numbers, return all possible permutations.

For example, [1, 2, 3] have the following permutations:
[
  [1, 2, 3],
  [1, 3, 2],
  [2, 1, 3],
  [2, 3, 1],
  [3, 1, 2],
  [3, 2, 1]
]

Problem provided by: https://leetcode.com/problems/permutations/
"""

def permute(nums):
  if nums == []:
    return [[]]
  permutations = []
  for idx,num in enumerate(nums):
    other_permutations = permute(nums[:idx] + nums[idx + 1:])
    permutations += map(lambda permutation: [num] + permutation, other_permutations)
  return permutations

print(permute([1, 2, 3]))
