"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key= lambda x: x.start)
        ends = [intervals[0].end]
        for i in range(1, len(intervals)):
            min_end, min_idx = ends[0], 0
            for j in range(len(ends)):
                if ends[j] < min_end:
                    min_end, min_idx = ends[j], j
            
            if intervals[i].start < min_end:
                ends.append(intervals[i].end)
            else:
                ends[min_idx] = intervals[i].end
        return len(ends)