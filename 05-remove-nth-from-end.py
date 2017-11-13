"""
Given a linked list, remove the nth node from the end of list and return its
head.

linked list:  1->2->3->4->5
nth:          0  1  2  3  4
nth from end: 5  4  3  2  1

Examples:
(1->2->3->4->5, 2) -> 1->2->3->5

Problem provided by: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

class Node:
  def __init__(self, value=0, next=None):
    self.value = value
    self.next = next
  def __repr__(self):
    if self.next is None:
      return str(self.value)
    return str(self.value) + '->' + repr(self.next)

def create_linked_list(arr):
  if not arr:
    return None
  return Node(arr[0], create_linked_list(arr[1:]))

def remove_nth_from_end(head, n):
  length = get_linked_list_length(head)
  return remove_nth(head, length - n)

def get_linked_list_length(head):
  length = 0
  tmp = head
  while tmp != None:
    length += 1
    tmp = tmp.next
  return length

def remove_nth(head, n):
  if head == None:
    return None
  if n == 0:
    return head.next
  head.next = remove_nth(head.next, n - 1)
  return head

def remove_nth_from_end_one_pass(head, n):
  if n < 1:
    return head
  leading = head
  trailing = head
  for i in range(n):
    if leading == None:
      return head
    leading = leading.next
  if leading == None:
    return head.next
  while leading != None:
    leading = leading.next
    if leading == None:
      trailing.next = trailing.next.next
      return head
    trailing = trailing.next
  return head

print(remove_nth_from_end(create_linked_list([1, 2, 3, 4, 5]), 2)) # 1->2->3->5
print(remove_nth_from_end(create_linked_list([1]), 1)) # None
print(remove_nth_from_end(create_linked_list([]), 0)) # None
print(remove_nth_from_end(create_linked_list([1, 2, 3, 4, 5]), 7)) # 1->2->3->4->5

print(remove_nth_from_end_one_pass(create_linked_list([1, 2, 3, 4, 5]), 2)) # 1->2->3->5
print(remove_nth_from_end_one_pass(create_linked_list([1]), 1)) # None
print(remove_nth_from_end_one_pass(create_linked_list([]), 0)) # None
print(remove_nth_from_end_one_pass(create_linked_list([1, 2, 3, 4, 5]), 7)) # 1->2->3->4->5
