#Conflicting Appointments (medium)
"""
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Time Complexity: O(Nlog(N))
Space Complexity: O(N)
"""
def can_attend_all_appointments(intervals):
  intervals.sort(key=lambda x: x[0])
  i = 0
  rando = True
  while rando and i<(len(intervals)-1):
    if intervals[i+1][0] <= intervals[i][1]:
      rando = False
    i += 1
  return rando
