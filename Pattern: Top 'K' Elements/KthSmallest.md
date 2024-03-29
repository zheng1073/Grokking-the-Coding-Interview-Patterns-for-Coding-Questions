# Problem Statement

Given an unsorted array of numbers, find Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

## Example 1:

Input: [1, 5, 12, 2, 11, 5], K = 3

Output: 5

Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

## Example 2:

Input: [1, 5, 12, 2, 11, 5], K = 4

Output: 5

Explanation: The 4th smallest number is '5', as the first three small numbers are [1, 2, 5].

## Example 3:

Input: [5, 12, 11, -1, 12], K = 3

Output: 11

Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].

##Code 
```python3
from heapq import *

def find_Kth_smallest_number(nums, k):
  maxHeap = []
  # put first k numbers in the max heap
  for i in range(k):
    heappush(maxHeap, -nums[i])

  # go through the remaining numbers of the array, if the number from the array is smaller than the
  # top(biggest) number of the heap, remove the top number from heap and add the number from array
  for i in range(k, len(nums)):
    if -nums[i] > maxHeap[0]:
      heappop(maxHeap)
      heappush(maxHeap, -nums[i])

  # the root of the heap has the Kth smallest number
  return -maxHeap[0]
```
