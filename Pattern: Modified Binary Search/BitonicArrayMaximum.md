# Problem Statement

Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

## Example 1:

Input: [1, 3, 8, 12, 4, 2]

Output: 12

Explanation: The maximum number in the input bitonic array is '12'.

## Example 2:

Input: [3, 8, 3, 1]

Output: 8

## Example 3:

Input: [1, 3, 8, 12]

Output: 12

## Code:
```python3
def find_max_in_bitonic_array(arr):
  start, end = 0, len(arr) - 1
  while start < end:
    mid = start + (end - start) // 2
    if arr[mid] > arr[mid + 1]:
      end = mid
    else:
      start = mid + 1

  # at the end of the while loop, 'start == end'
  return arr[start]

```
