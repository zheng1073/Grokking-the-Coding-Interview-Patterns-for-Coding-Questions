#Reverse Level Order Traversal (easy)
"""
Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest level comes first. 
You should populate the values of all nodes in each level from left to right in separate sub-arrays.

Time Complexity: O(N)
Space Complexity: O(W)
"""
from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = deque()
  # TODO: Write your code here
  if root == None:
    return result
  
  queue = deque()
  queue.append(root)
  
  while queue:
    currentLevel = []
    for _ in range(len(queue)):
      currentValue = queue.popleft()
      currentLevel.append(currentValue.val)
      if currentValue.left:
        queue.append(currentValue.left)
      if currentValue.right:
        queue.append(currentValue.right)
    
    result.appendleft(currentLevel)
  return result
