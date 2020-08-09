
#Sum of Path Numbers (medium)
"""
Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. 
Find the total sum of all the numbers represented by all paths.

Time Complexity: O(N)
Space Complexity: O(N)
"""
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root):
  # TODO: Write your code here
  return sum_of_paths(root, 0) 

def sum_of_paths(currentNode, totalSum):
  if currentNode is None:
    return 0
  
  totalSum = 10 * totalSum + currentNode.val
  
  if currentNode.left is None and currentNode.right is None:
    return totalSum
  
  return sum_of_paths(currentNode.left, totalSum) + sum_of_paths(currentNode.right, totalSum)

