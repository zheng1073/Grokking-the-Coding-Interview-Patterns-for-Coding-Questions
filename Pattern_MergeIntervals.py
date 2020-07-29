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

Time Complexity: O(logN)
Space Complexity: O(1)
"""
from __future__ import print_function 
