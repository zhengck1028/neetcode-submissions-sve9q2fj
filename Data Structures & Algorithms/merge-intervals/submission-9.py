class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])
        last_end = intervals[0][1]
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s <= last_end:
                res[-1][1] = max(last_end, e)
            else:
                res.append([s, e])
            last_end = max(last_end, e)
        return res