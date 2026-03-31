class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        ns = newInterval[0]
        ne = newInterval[1]
        for i in range(len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            if e < newInterval[0]:
                res.append([s, e])
            elif s <= newInterval[1]:
                ns = min(s, ns)
                ne = max(e, ne)
            else:
                res.append([ns, ne])
                res.extend(intervals[i:])
                return res
        res.append([ns, ne])
        return res