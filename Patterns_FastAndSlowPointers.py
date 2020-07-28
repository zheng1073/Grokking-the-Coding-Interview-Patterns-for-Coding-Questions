"""
Also known as Hare and Tortoise, is a pointer algorithm that uses two pointers which move through the array (or sequence/LinkedList) at different speeds.

Useful with cyclic LinkedList or Arrays 
"""

#LinkedList Cycle (easy)
  """  
  Given the head of a Singly LinkedList, determine if LinkedList has a cycle or not.
  
  Time Complexity : O(N)
  Space Complexity : O(1)
  """
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
  
def has_cycle(head):
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
    if fast == slow:
      return True
  return False

 """  
  Given the head of a LinkedList with a cycle, find the length of the cycle.
  
  Time Complexity : O(N)
  Space Complexity : O(1)
  """
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
  
def find_cycle_length(head):
  slow, fast = head, head
  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
    if fast == slow:
      return calculate_cycle_length(slow)
  return 0

def calculate_cycle_length(slow):
  current = slow
  cycle_length = 0
  while True:
    current = current.next
    cycle_length += 1
    if current == slow: #reached the beginnig of the cycle again
      break
  return cycle_length

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

#Happy Number (medium)
"""
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, 
leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

Time Complexity: O(logN)
Space Complexity: O(1)
"""
def find_happy_number(num):
  slow, fast = num, num
  while True:
    slow = find_square_sum(slow)  # move one step
    fast = find_square_sum(find_square_sum(fast))  # move two steps
    if slow == fast:  # found the cycle
      break
  return slow == 1  # see if the cycle is stuck on the number '1'


def find_square_sum(num):
  _sum = 0
  while (num > 0):
    digit = num % 10
    _sum += digit * digit
    num //= 10
  return _sum 

#Middle of the LinkedList (easy)
"""
Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

If the total number of nodes in the LinkedList is even, return the second middle node.

Time Complexity:
Space Complexity:
"""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def find_middle_of_linked_list(head):
  slow, fast = head, head
  while (fast is not None and fast.next is not None):
    slow = slow.next
    fast = fast.next.next
  return slow
