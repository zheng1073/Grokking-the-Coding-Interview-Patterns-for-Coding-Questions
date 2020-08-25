# Problem Statement

Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

## Example 1:

Input: [3, 1, 5, 12, 2, 11], K = 3

Output: [5, 12, 11]

## Example 2:

Input: [5, 12, 11, -1, 12], K = 3

Output: [12, 11, 12]

## Code:
```python3
from heapq import *

def find_k_largest_numbers(nums, k):
  #create the heap
  minHeap = []
  #inititalize heap size with K elements
  for i in range(k):
    heappush(minHeap, nums[i])
  #compare other values in array to see what's largest
  for i in range(k, len(nums)):
    if nums[i] > minHeap[0]:
      heapreplace(minHeap, nums[i])
  return list(minHeap)
```
