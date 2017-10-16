"""
You are given an array of n integers and a number k. Determine whether there is
a pair of elements in the array that sums to exactly k. For example, given the
array [1, 3, 7] and k = 8, the answer is "yes", but given k = 6 the answer is
"no."

Problem provided by: https://web.stanford.edu/class/cs9/lectures/04/Two-Sum.pdf
"""

def two_sum(numbers, target):
  for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
      if numbers[i] + numbers[j] == target:
        return True
  return False

def two_sum2(numbers, target):
  s = set()
  for num in numbers:
    if (target - num) in s:
      return True
    s.add(num)
  return False

print(two_sum2([1, 3, 7], 8) == True)
print(two_sum2([1, 3, 7], 6) == False)
print(two_sum2([], 1) == False)
print(two_sum2([1, 1], 2) == True)
print(two_sum2([1], 1) == False)
