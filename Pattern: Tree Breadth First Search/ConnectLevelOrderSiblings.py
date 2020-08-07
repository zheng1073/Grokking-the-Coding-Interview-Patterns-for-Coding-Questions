
#Connect Level Order Siblings (medium)
"""
Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.

Time Complexity: O(N)
Space Complexity: O(W)
"""
from __future__ import print_function
from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # level order traversal using 'next' pointer
  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot
      nextLevelRoot = None
      while current:
        print(str(current.val) + " ", end='')
        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left
          elif current.right:
            nextLevelRoot = current.right
        current = current.next
      print()

def connect_level_order_siblings(root):
  if root is None:
    return

  queue = deque()
  queue.append(root)
  while queue:
    previousNode = None
    levelSize = len(queue)
    # connect all nodes of this level
    for _ in range(levelSize):
      currentNode = queue.popleft()
      if previousNode:
        previousNode.next = currentNode
      previousNode = currentNode

      # insert the children of current node in the queue
      if currentNode.left:
        queue.append(currentNode.left)
      if currentNode.right:
        queue.append(currentNode.right)
