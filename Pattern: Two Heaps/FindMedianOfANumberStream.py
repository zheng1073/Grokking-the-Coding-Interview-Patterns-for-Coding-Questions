#Find the Median of a Number Stream (medium)
"""
Design a class to calculate the median of a number stream. The class should have the following two methods:

  insertNum(int num): stores the number in the class
  findMedian(): returns the median of all numbers inserted in the class
  
If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.
"""
from heapq import *

class MedianOfAStream:
  #contain first half of numbers
  maxHeap = []
  #contain second half numbers
  minHeap = []
  
  def insert_num(self, num):
    if not self.maxHeap or -self.maxHeap[0] >= num:
      heappush(self.maxHeap, -num)
    else:
      heappush(self.minHeap, num)

    # either both the heaps will have equal number of elements or max-heap will have one
    # more element than the min-heap
    if len(self.maxHeap) > len(self.minHeap) + 1:
      heappush(self.minHeap, -heappop(self.maxHeap))
    elif len(self.maxHeap) < len(self.minHeap):
      heappush(self.maxHeap, -heappop(self.minHeap))

  def find_median(self):
    if len(self.maxHeap) == len(self.minHeap):
      # we have even number of elements, take the average of middle two elements
      return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0

    # because max-heap will have one more element than the min-heap
    return -self.maxHeap[0] / 1.0
