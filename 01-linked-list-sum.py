"""
You are given two non-empty linked lists that represent integers. A linked
list of 1->2->3 represents the integer 321. Write a function to sum two of
these linked lists and return the sum as a linked list. For example, given
the linked lists, 1->2->3 and 2->4->7, the sum is 3->6->0->1.

Problem adapted from: https://leetcode.com/problems/add-two-numbers/
"""

class Node:
  def __init__(self, value=0, next=None):
    self.value = value
    self.next = next

def linked_list_sum_iterative(list1, list2):
  res = Node()
  p1 = list1
  p2 = list2
  curr = res
  carry = 0
  while p1 is not None or p2 is not None or carry != 0:
    sum = carry
    if p1:
      sum += p1.value
      p1 = p1.next
    if p2:
      sum += p2.value
      p2 = p2.next
    curr.value = sum % 10
    carry = sum // 10
    if p1 is not None or p2 is not None or carry != 0:
      curr.next = Node()
      curr = curr.next
  return res

def linked_list_sum(list1, list2, carry=0):
  if list1 is None and list2 is None and carry == 0:
    return None
  next1 = None
  next2 = None
  sum = carry
  if list1:
    sum += list1.value
    next1 = list1.next
  if list2:
    sum += list2.value
    next2 = list2.next
  return Node(sum % 10, linked_list_sum(next1, next2, sum // 10))
