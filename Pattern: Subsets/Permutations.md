# Problem Statement

Given a set of distinct numbers, find all of its permutations.

**Permutation** is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

  1. {1, 2, 3}
  2. {1, 3, 2}
  3. {2, 1, 3}
  4. {2, 3, 1}
  5. {3, 1, 2}
  6. {3, 2, 1}
  
If a set has ‘n’ distinct elements it will have n!n! permutations.

**Example 1:**

Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]

**Code:**
```python3
def generate_permutations(nums):
  result = []
  generate_permutations_recursive(nums, 0, [], result)
  return result


def generate_permutations_recursive(nums, index, currentPermutation, result):
  if index == len(nums):
    result.append(currentPermutation)
  else:
    # create a new permutation by adding the current number at every position
    for i in range(len(currentPermutation)+1):
      newPermutation = list(currentPermutation)
      newPermutation.insert(i, nums[index])
      generate_permutations_recursive(
        nums, index + 1, newPermutation, result)

```
