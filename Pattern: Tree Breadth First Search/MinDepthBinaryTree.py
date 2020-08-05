#Minimum Depth of a Binary Tree (easy)
"""
Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.

Time Complexity: O(N)
Space Complexity: O(W)
"""
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
  if root is None:
    return 0

  queue = deque()
  queue.append(root)
  minimumTreeDepth = 0
  while queue:
    minimumTreeDepth += 1
    levelSize = len(queue)
    for _ in range(levelSize):
      currentNode = queue.popleft()

      # check if this is a leaf node
      if not currentNode.left and not currentNode.right:
        return minimumTreeDepth

      # insert the children of current node in the queue
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)
