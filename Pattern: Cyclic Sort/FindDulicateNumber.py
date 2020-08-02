#Find the Duplicate Number (easy)
"""
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one duplicate but it can be repeated multiple times. 
Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

Time Complexity: O(N)
Space Complexity: O(1)
"""
def find_duplicate(nums):
  i = 0
  while i < len(nums):
    if nums[i] != i + 1:
      j = nums[i] - 1
      if nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]  # swap
      else:  # we have found the duplicate
        return nums[i]
    else:
      i += 1

  return -1


def find_duplicate(nums):
  # TODO: Write your code here
  i = 0
  rando = []
  rando2 = True
  while i < len(nums) and rando2:
    if nums[i] not in rando:
      rando.append(nums[i])
      i += 1
    else:
      rando2 = False
      return nums[i]  
  return -1
