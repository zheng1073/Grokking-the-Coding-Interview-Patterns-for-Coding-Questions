# Subsets (easy)

**Problem Statement**

Given a set with distinct elements, find all of its distinct subsets.

**Example 1:**

Input: [1, 3]

Output: [], [1], [3], [1,3]

**Example 2:**

Input: [1, 5, 3]

Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]

Code:

```python3
def find_subsets(nums):
  #create an empty list to put all subsets
  subsets = []
  #add empty subset
  subsets.append([])
  for currentNumber in nums:
    n = len(subsets)
    for i in range(n):
      set = list(subsets[i])
      set.append(currentNumber)
      subsets.append(set)
      
  return subsets

```
