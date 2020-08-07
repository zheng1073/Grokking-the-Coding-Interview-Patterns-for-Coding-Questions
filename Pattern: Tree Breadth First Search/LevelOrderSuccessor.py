
#Level Order Successor (easy)
"""
Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears 
right after the given node in the level order traversal.

Time Complexity: O(N)
Space Complexity: O(W)
"""
from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  if root is None:
    return None

  queue = deque()
  queue.append(root)
  while queue:
    currentNode = queue.popleft()
    # insert the children of current node in the queue
    if currentNode.left:
      queue.append(currentNode.left)
    if currentNode.right:
      queue.append(currentNode.right)

    # break if we have found the key
    if currentNode.val == key:
      break

  return queue[0] if queue else None
