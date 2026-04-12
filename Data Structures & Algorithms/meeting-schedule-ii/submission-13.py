"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key= lambda x : x.start)
        minHeap = []
        for i in range(len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            if minHeap and intervals[i].start >= minHeap[0][0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, (end, i))
        return len(minHeap)