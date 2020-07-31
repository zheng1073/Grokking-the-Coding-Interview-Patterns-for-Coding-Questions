#Start of LinkedList Cycle (medium)
"""
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
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
      print(temp.value, end='')
      temp = temp.next
    print()
    
def find_cycle_start(head):
  cycle_length = 0
  #find the LinkedList cycle
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
    if slow == fast:
      cycle_length = calculate_cycle_length(slow)
      break
  return find_start(head, cycle_length)

def calculate_cycle_length(slow):
  current = slow
  cycle_length = 0
  while True:
    current = current.next
    cycle_length += 1
    if cyrrent == slow:
      break
  return cycle_length

def find_start(head, cycle_length):
  pointer1 = head
  pointer2 = head
  while cycle_length > 0:
    pointer2 = pointer2.next
    cycle_length -= 1
  while pointer1 != pointer2:
    pointer1 = pointer1.next
    pointer2 = pointer2.next
  return pointer1
