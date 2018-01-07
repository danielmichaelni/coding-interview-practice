"""
Merge two sorted linked lists and return it as a new list.

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Problem provided by: https://leetcode.com/problems/merge-two-sorted-lists/
"""

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
    def __repr__(self):
        if self.next is None:
            return str(self.value)
        return str(self.value) + '->' + repr(self.next)

def merge(l1, l2):
    if l1 is None and l2 is None:
        return None
    elif l1 is None:
        return Node(l2.value, merge(l1, l2.next))
    elif l2 is None:
        return Node(l1.value, merge(l1.next, l2))
    elif l1.value < l2.value:
        return Node(l1.value, merge(l1.next, l2))
    else:
        return Node(l2.value, merge(l1, l2.next))

print(merge(None,
            None)) # None
print(merge(None,
            Node(1))) # 1
print(merge(Node(1, Node(2, Node(4))),
            Node(1, Node(3, Node(4))))) # 1->1->2->3->4->4
