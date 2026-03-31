class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        res = 0
        intervals.sort(key=lambda x : (x[0], x[1]))
        last_end = intervals[0][1]
        for i in range(1, len(intervals)):
            cur_start = intervals[i][0]
            if cur_start < last_end:
                res += 1
                last_end = min(last_end, intervals[i][1])
            else:
                last_end = intervals[i][1]
        
        return res