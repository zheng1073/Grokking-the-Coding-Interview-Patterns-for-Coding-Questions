#Path with Given Sequence (medium)
"""
Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.

Time Complexity: O(N^2)
Space Complexity: O(NlogN)
"""
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_path(root, sequence):
  # TODO: Write your code here
  if not root:
    return len(sequence) == 0

  return find_path_recursive(root, sequence, 0)


def find_path_recursive(currentNode, sequence, sequenceIndex):

  if currentNode is None:
    return False

  seqLen = len(sequence)
  if sequenceIndex >= seqLen or currentNode.val != sequence[sequenceIndex]:
    return False

  # if the current node is a leaf, add it is the end of the sequence, we have found a path!
  if currentNode.left is None and currentNode.right is None and sequenceIndex == seqLen - 1:
    return True

  # recursively call to traverse the left and right sub-tree
  # return true if any of the two recursive call return true
  return find_path_recursive(currentNode.left, sequence, sequenceIndex + 1) or \
         find_path_recursive(currentNode.right, sequence, sequenceIndex + 1)
  
  
