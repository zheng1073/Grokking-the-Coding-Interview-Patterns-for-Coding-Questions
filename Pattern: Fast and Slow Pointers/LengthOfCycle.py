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
