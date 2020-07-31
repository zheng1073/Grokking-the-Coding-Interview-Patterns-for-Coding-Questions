#Insert Intervals (medium)
"""
Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all 
necessary intervals to produce a list that has only mutually exclusive intervals.

Time Complexity: O(N)
Space Complexity: O(N)
"""

def insert(intervals, new_interval):
  merged = []
  i, start, end = 0, 0, 1
  
  #all intervals that come before the 'new_interval'
  while i < len(intervals) and intervals[i][end] < new_interval[start]:
    merged.append(intervals[i])
    i += 1
    
  #all intervals that overlap with 'new_interval'
  while i < len(intervals) and intervals[i][start] <= new_interval[end]:
    new_interval[start] = min(intervals[i][start], new_interval[start])
    new_interval[end] = max(intervals[i][end], new_interval[end])
    i += 1
  
  merged.append(new_interval)
  
  #all remaining intervals
  while i < len(intervals):
    merged.append(intervals[i])
    i += 1
    
  return merged
