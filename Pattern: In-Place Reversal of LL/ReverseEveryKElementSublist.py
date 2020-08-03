#Reverse every K-element Sub-List (medium)
"""
Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

Time Complexity: O(N)
Space Complexity: O(1)
"""
from __future__ import print_function

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()

def reverse_every_k_elements(head, k):
  if k <= 1 or head is None:
    return head

  current, previous = head, None
  while True:
    last_node_of_previous_part = previous
    # after reversing the LinkedList 'current' will become the last node of the sub-list
    last_node_of_sub_list = current
    next = None  # will be used to temporarily store the next node
    i = 0
    while current is not None and i < k:  # reverse 'k' nodes
      next = current.next
      current.next = previous
      previous = current
      current = next
      i += 1

    # connect with the previous part
    if last_node_of_previous_part is not None:
      last_node_of_previous_part.next = previous
    else:
      head = previous

    # connect with the next part
    last_node_of_sub_list.next = current

    if current is None:
      break
    previous = last_node_of_sub_list
  return head
