"""
Deals with overlapping intervals. In a lot of problems involving intervals, we either need to find overlapping intervals or merge intervals if they overlap.

Six ways 2 intervals can relate to each other.
  1. 'a' and 'b' do not overlap; 'a' before 'b'
  2. 'a' and 'b' overlap and 'b' ends after 'a'
  3. 'a' completely overlaps 'b'
  4. 'a' and 'b' overlap, 'a' ends after 'b' 
  5. 'b' completely overlaps 'a'
  6. 'a' and 'b' do not overlap; 'b' before 'a'
"""

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

#Insert Interval (medium)
"""
Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary 
gintervals to produce a list that has only mutually exclusive intervals.

Time Complexity: O(NlogN)
Space Complexity: O(N)
"""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
