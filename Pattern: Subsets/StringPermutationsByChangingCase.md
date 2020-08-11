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
def find_letter_case_string_permutations(str):
  permutations = []
  permutations.append(str)
  # process every character of the string one by one
  for i in range(len(str)):
    if str[i].isalpha():  # only process characters, skip digits
      # we will take all existing permutations and change the letter case appropriately
      n = len(permutations)
      for j in range(n):
        chs = list(permutations[j])
        # if the current character is in upper case, change it to lower case or vice versa
        chs[i] = chs[i].swapcase()
        permutations.append(''.join(chs))

  return permutations
```
