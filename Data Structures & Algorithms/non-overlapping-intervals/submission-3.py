class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        
        lastend = intervals[0][1]
        i = 1
        while i<len(intervals):
            if intervals[i][0] < lastend:
                res += 1
                lastend = min(lastend, intervals[i][1])
                # 【关键修正】：贪心策略
                # 两个打架了，谁结束得早，谁留下来（因为对后面影响小）
            else:
                lastend = intervals[i][1]
            i += 1
        return res