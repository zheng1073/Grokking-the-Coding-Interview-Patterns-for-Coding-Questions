XOR is a logical bitwise operator that returns 0 (false) if both bits are the same and returns 1 (true) otherwise. In other words, it only returns 1 if exactly one bt is set to 1 out of the two bits in comparison.

A | B | A xor B
-- | -- | --
0 | 0 | 0
0 | 1 | 1
1 | 1 | 0
1 | 1 | 0

It is surprising to know that approaches that the XOR operator enables us to solve certain problems. For example, let's take a look at the following problem:

_Given an array of n-1 integers in the range from 1 to n, find the one number that is missing from the array._ 

**Example**

Input: 1, 5, 2, 6, 4

Answer: 3

__How can we use XOR to help?__

An important property of XOR is that it returns 0 if both the bits in the comparison are the same. In the other words, XOR of a number with itself is always 0. This means that if we XOR all the numbers in the input array with all numbers from the range 11 to nn then each number in the input is going to get zeroed out except the missing number. Following are the set of steps to find the missing number using XOR:

1. XOR all the numbers from 1 to n, let's call it x1.
1. XOR all the numbers in the inputer array, let's call it x2.
1. The missing number can be found by x1 XOR x2.

**Code:**
```python3
def find_missing_number(arr):
  n = len(arr) + 1
  # xl represents XOR of all values from 1 to n
  x1 = 1 ^ n
  
  #x2 represents XOR of all values in arr
  x2 = arr[0]
  for i in range(1, n-1):
    x2 = x2 ^ arr[i]
    
  # missing number is the xor of xl and x2
  return x1 ^ x2
```

