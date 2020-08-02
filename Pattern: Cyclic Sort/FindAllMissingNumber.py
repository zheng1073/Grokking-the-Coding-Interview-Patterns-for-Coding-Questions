#Find All Missing Number (easy)
"""
We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means some numbers will be missing. 
Find all those missing numbers.

Time Complexity: O(N)
Space Complexity: O(1)
"""
def find_missing_numbers(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  missingNumbers = []

  for i in range(len(nums)):
    if nums[i] != i + 1:
      missingNumbers.append(i + 1)

  return missingNumbers


def find_missing_numbers(nums):
  missingNumbers = []
  # TODO: Write your code here
  i = 0
  while i < len(nums):
    if i+1 not in nums:
      missingNumbers.append(i+1)
    i += 1
  return missingNumbers
