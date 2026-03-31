"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key= lambda x:x.start)
        minheap = []
        for i in intervals:
            if minheap and i.start >= minheap[0]:
                heapq.heappop(minheap)
            heapq.heappush(minheap, i.end)
        return len(minheap)