"""
Given a string, find the longest palindromic substring.

Examples:
"babad" -> "bab" or "aba"
"cbbd" -> "bb"

Problem provided by: https://leetcode.com/problems/longest-palindromic-substring/
"""

def longest_palindromic_substring_brute_force(string):
  longest = ''
  for i in range(len(string)):
    for j in range(i, len(string)):
      if string[i:j] == string[i:j][::-1] and j - i > len(longest):
        longest = string[i:j]
  return longest

def longest_palindromic_substring(string):
  start = 0
  end = 0
  for i in range(len(string)):
    left, right = helper(string, i, i)
    if right - left > end - start:
      start = left
      end = right
    left, right = helper(string, i, i + 1)
    if right - left > end - start:
      start = left
      end = right
  return string[start:end + 1]

def helper(string, left, right):
  if right >= len(string):
    return (0, 0)
  start = left
  end = right
  while start >= 0 and end < len(string) and string[start] == string[end]:
    start -= 1
    end += 1
  return (start + 1, end - 1)

print(longest_palindromic_substring('babad') == 'bab')
print(longest_palindromic_substring('cbbd') == 'bb')
