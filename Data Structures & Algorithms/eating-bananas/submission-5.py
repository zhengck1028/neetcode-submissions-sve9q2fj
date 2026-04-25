class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = h
        while l <= r:
            m = (l+r) // 2
            need = 0
            for p in piles:
                need += math.ceil(float(p/m))
            if need > h:
                l = m + 1
            else:
                res = m
                r = m -1
        return res