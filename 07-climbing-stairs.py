"""
You are climbing a stair case. It takes n steps to reach the top. Each time you
can either climb 1 or 2 steps. In how many distinct ways can you climb to the
top?

Example:
When n = 3, there are three ways to climb to the top:
1) 1 step + 1 step + 1 step
2) 1 step + 2 steps
3) 2 steps + 1 step

Problem provided by: https://leetcode.com/problems/climbing-stairs/
"""

def climb_stairs(n):
  if n == 0:
    return 1
  if n < 0:
    return 0
  return climb_stairs(n - 1) + climb_stairs(n - 2)

def climb_stairs_with_memo(n):
  memo = {}
  return climb_stairs_helper(n, memo)

def climb_stairs_helper(n, memo):
  if n == 0:
    return 1
  if n < 0:
    return 0
  if n in memo:
    return memo[n]
  memo[n] = climb_stairs_helper(n - 1, memo) + climb_stairs_helper(n - 2, memo)
  return memo[n]

print(climb_stairs(3) == 3)
print(climb_stairs(0) == 1)
print(climb_stairs(-1) == 0)
print(climb_stairs(20) == 10946)

print(climb_stairs_with_memo(3) == 3)
print(climb_stairs_with_memo(0) == 1)
print(climb_stairs_with_memo(-1) == 0)
print(climb_stairs_with_memo(20) == 10946)
