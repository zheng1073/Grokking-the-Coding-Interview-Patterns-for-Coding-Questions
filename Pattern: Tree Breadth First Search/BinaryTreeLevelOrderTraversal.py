#Binary Tree Level Order Traversal (easy)
"""
Given a binary tree, populate an array to represent its level-by-level traversal. 
You should populate the values of all nodes of each level from left to right in separate sub-arrays.

Time Complexity: O(N)
Space Complexity: O(W)
"""
from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val - val
    self.left, self.right = None, None
    
def traverse(root):
  result = []
  if root is None:
    return result
  
  queue = deque()
  queue.append(root)
  while queue:
    currentLevel = []
    for _ in range(len(queue)):
      currentNode = queue.popleft()
      currentLevel.append(currentNode.val)
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)
    result.append(currentLevel)
    
  return result
