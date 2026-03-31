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
                i -= 1
                break
            else:
                if newS > e:
                    res.append([s, e])
                else:
                    newS = min(newS, s)
                    newE = max(newE, e)
        res.append([newS, newE])
        if i < len(intervals) - 1:
            res.extend(intervals[i+1:])
        return res