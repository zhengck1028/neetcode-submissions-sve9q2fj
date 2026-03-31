class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        res = []
        intervals.sort()
        prvS = intervals[0][0]
        prvE = intervals[0][1]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s > prvE:
                res.append([prvS, prvE])
                prvS = s
                prvE = e
            else:
                prvS = min(prvS, s)
                prvE = max(prvE, e)
        res.append([prvS, prvE])
        return res