#All Paths for a Sum (medium)
"""
Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.

Time Complexity: O(N^2)
Space Complexity: O(NlogN)
"""
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, required_sum):
  allPaths = []
  find_paths_recursive(root, required_sum, [], allPaths)
  return allPaths


def find_paths_recursive(currentNode, required_sum, currentPath, allPaths):
  if currentNode is None:
    return

  # add the current node to the path
  currentPath.append(currentNode.val)

  # if the current node is a leaf and its value is equal to required_sum, save the current path
  if currentNode.val == required_sum and currentNode.left is None and currentNode.right is None:
    allPaths.append(list(currentPath))
  else:
    # traverse the left sub-tree
    find_paths_recursive(currentNode.left, required_sum -
                         currentNode.val, currentPath, allPaths)
    # traverse the right sub-tree
    find_paths_recursive(currentNode.right, required_sum -
                         currentNode.val, currentPath, allPaths)

  # remove the current node from the path to backtrack,
  # we need to remove the current node while we are going up the recursive call stack.
  del currentPath[-1]
