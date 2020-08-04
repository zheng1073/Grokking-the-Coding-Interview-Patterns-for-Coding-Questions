#Zipzag Traversal (medium)
"""
Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of all nodes of the first level from left to right, 
then right to left for the next level and keep alternating in the same manner for the following levels.

Time Complexity: O(N)
Space Complexity: O(W)
"""
from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = []
  if root is None:
    return result
  
  queue = deque()
  queue.append(root)
  leftToRight = True
  while queue:
    levelSize = len(queue)
    currentLevel = deque()
    for _ in range(levelSize):
      currentNode = queue.popleft()

      # add the node to the current level based on the traverse direction
      if leftToRight:
        currentLevel.append(currentNode.val)
      else:
        currentLevel.appendleft(currentNode.val)

      # insert the children of current node in the queue
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)

    result.append(list(currentLevel))
    # reverse the traversal direction
    leftToRight = not leftToRight

  return result
