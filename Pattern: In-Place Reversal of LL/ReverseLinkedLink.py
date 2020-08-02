
#Reverse a LinkedList (easy)
"""
Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.

Time Complexity: O(N)
Space Complexity: O(1)
"""
from __future__ import print_function

class Node:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next
   
  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
     print()
    
  def reverse(head):
    previous, current, next = None, head, None
    while current is not None:
      next = current.next
      current.next = previous
      previous = current
      current = next
    return head
