#Merge Intervals (medium)
"""
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
Time Complexity: O(NlogN)
Space Complexity: O(N)
"""
from __future__ import print_function 

class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end
  
  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')
    
def merge(intervals):
  #edge case if there is only one interval
  if len(intervals) < 2:
    return intervals
  
  #sort interval based on the start
  intervals.sort(key=lambda x: x.start)
  
  mergedIntervals = []
  start = intervals[0].start
  end = intervals[0].end
  for i in range(1, len(intervals)):
    interval = intervals[i]
    #check if second interval is in our first interval
    if interval.start <= end:
      end = max(interval.end, end)
    else:
      mergedIntervals.append(Interval(start, end))
      start = interval.start
      end = interval.end
  mergedIntervals.append(Interval(start, end))
  return mergedIntervals
