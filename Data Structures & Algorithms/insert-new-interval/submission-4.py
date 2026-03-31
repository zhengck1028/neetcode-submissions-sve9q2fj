class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        res = []
        newS = newInterval[0]
        newE = newInterval[1]
        for i in range(len(intervals)):
            s, e = intervals[i][0], intervals[i][1]
            if newE < s:
                res.append([newS, newE])
                return res + intervals[i:]
            else:
                if newS > e:
                    res.append([s, e])
                else:
                    newS = min(newS, s)
                    newE = max(newE, e)
        res.append([newS, newE])
        return res