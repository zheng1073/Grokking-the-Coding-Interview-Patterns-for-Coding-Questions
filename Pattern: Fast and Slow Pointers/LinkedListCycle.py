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
