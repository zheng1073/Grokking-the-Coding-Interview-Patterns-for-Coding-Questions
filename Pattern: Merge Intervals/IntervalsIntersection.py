#Intervals Intersection (medium)
"""
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Time Complexity: O(N + M)
Space Complexity: O(1)
"""
def merge(intervals_a, intervals_b):
  result = []
   i, j, start, end = 0, 0, 0, 1
   while i < len(intervals_a) and j < len(intervals_b):
    a_over_b = intervals_a[i][start] >= intervals_b[j][start] and intervals_a[i][start] <= intervals_b[j][end]
    b_over_a = intervals_a[i][start] <= intervals_b[j][start] and intervals_b[j][start] <= intervals_a[i][end]

    if a_over_b or b_over_a:
      result.append([max(intervals_a[i][start], intervals_b[j][start]), min(intervals_a[i][end], intervals_b[j][end])])

    if intervals_b[j][end] > intervals_a[i][end]:
      i += 1
    else:
      j += 1
      
  return result
