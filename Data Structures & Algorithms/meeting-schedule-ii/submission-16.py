"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # [(0, 40), (5, 10), (15, 20)]
        # room #1 : i=0, end = 40
        # room #2 : i=1, end=10; i=2, end=20

        intervals.sort(key = lambda x : x.start)
        minHeap = []
        for i in range(len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            if minHeap and start >= minHeap[0]: # do not use while here
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, end)
        return len(minHeap)
