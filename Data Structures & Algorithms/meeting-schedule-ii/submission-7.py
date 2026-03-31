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
        intervals.sort(key= lambda x: (x.start, x.end))
        rooms = [intervals[0].end]
        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i].start, intervals[i].end
            min_end = min(rooms)
            min_end_idx = rooms.index(min_end)
            if cur_start < min_end:
                rooms.append(cur_end)
            else:
                rooms[min_end_idx] = cur_end
        return len(rooms)