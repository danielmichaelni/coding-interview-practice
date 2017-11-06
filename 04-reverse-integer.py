"""
Reverse the digits of an integer.

Examples:
123 -> 321
-123 -> -321

Problem provided by: https://leetcode.com/problems/reverse-integer/
"""

def reverse_integer(x):
  reversed = 0
  sign = 1 if x > 0 else -1
  tmp = abs(x)
  while tmp != 0:
    reversed = reversed * 10 + tmp % 10
    tmp = tmp // 10
  return sign * reversed

print(reverse_integer(123) == 321)
print(reverse_integer(-123) == -321)
