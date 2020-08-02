#Find the Missing Number (easy)
"""
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, 
find the missing number.

Time Complexity: O(N)
Space Complexity: O(1)
"""
def find_missing_number(nums):
  i, n = 0, len(nums)
  while i < n:
    j = nums[i]
    if nums[i] < n and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  # find the first number missing from its index, that will be our required number
  for i in range(n):
    if nums[i] != i:
      return i

  return n
