class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hm = {}
        for i in range(len(s)):
            ch = s[i]
            if ch not in hm:
                hm[ch] = [i, i]
            else:
                hm[ch][1] = i
        
        intervals = list(hm.values())
        intervals.sort()
        res = []
        last_start, last_end = 0, 0
        for start, end in intervals:
            if start <= last_end:
                last_end = max(last_end, end)
            else:
                res.append(last_end - last_start + 1)
                last_start, last_end = start, end
        res.append(last_end - last_start + 1)
        return res