class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        hm = collections.OrderedDict() # cha : [start, end]
        for i, c in enumerate(s):
            if c not in hm:
                hm[c] = [i, i]
            else:
                hm[c][1] = i
        
        intervals = list(hm.values())
        intervals.sort()
        p_s, p_e = hm.popitem(last= False)[1]
        while hm:
            c_s, c_e = hm.popitem(last= False)[1]
            if c_s < p_e:
                p_e = max(p_e, c_e)
            else:
                res.append(p_e - p_s + 1)
                p_s = c_s
                p_e = c_e
        res.append(p_e - p_s + 1)
        return res