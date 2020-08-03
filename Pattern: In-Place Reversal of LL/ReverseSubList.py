#Reverse a Sub-List (Medium)
"""
Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.

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

def reverse_sub)list(head, p, q):
  #if p = q, you don't need to reverse anything
  if p == q:
    return head
  
  current, previous = head, None
  i = 0
  while current is not None and i < p -1:
    previous = current
    current = current.next
    i += 1
  
  last_node_of_first_part = previous
  last_node_of_sub_list = current
  i = 0
  
  while current is not None and i < q - p + 1:
    next = current.next
    current.next = previous
    previous = current
    current = next
    i += 1
    
  if last_node_of_first_part is not None:
    last_node_of_first_part.next = previous
  else:
    head = previous
    
  last_node_of_sub_list.next = current
  return head

