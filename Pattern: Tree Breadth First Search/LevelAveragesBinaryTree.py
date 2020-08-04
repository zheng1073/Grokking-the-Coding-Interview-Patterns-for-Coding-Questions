#Level Averages in a Binary Tree (easy)
"""
Given a binary tree, populate an array to represent the averages of all of its levels.

Time Complexity: O(N)
Space Complexity: O(W)
"""
from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
  result = []
  # TODO: Write your code here
  if root is None:
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
    average = sum(currentLevel) / len(currentLevel)
    result.append(average)
    
  return result
