"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The parentheses must close in the correct order, "()" and "()[]{}" are all
valid but "(]" and "([)]" are not.
"""

def is_valid(parens):
  stack = []
  matches = {
    ')': '(',
    '}': '{',
    ']': '['
  }
  for p in parens:
    if p == '(' or p == '{' or p == '[':
      stack.append(p)
    elif stack == [] or stack.pop() != matches[p]:
      return False
  return stack == []

print(is_valid('()') == True)
print(is_valid('()[]{}') == True)
print(is_valid('(]') == False)
print(is_valid('([)]') == False)
print(is_valid('(()[])') == True)
print(is_valid(')') == False)
