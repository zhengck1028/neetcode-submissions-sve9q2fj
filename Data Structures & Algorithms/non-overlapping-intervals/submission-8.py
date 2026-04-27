class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[1])
        last_end = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < last_end:
                res += 1
                continue
            else:
                last_end = end
        return res
