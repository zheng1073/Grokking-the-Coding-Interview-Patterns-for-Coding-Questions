#Binary Tree Path Sum (easy)
"""
Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.

Time Complexity: O(N)
Space Complexity: O(N)
"""
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def has_path(root, sum):
  # TODO: Write your code here
  if root is None:
   return False
  
  #if current node is a leaf and its value is equal to the sum, we've found a path
  if root.val == sum and root.left is None and root.right is None:
   return Trye
  
  return has_path(root.left, sum-root.val) or has_path(root.right, sum-root.val)
  return False
