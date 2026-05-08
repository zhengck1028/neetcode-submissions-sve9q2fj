class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = float("inf")
        while l <= r:
            m = (l + r) // 2
            total = 0
            for p in piles:
                total += math.ceil(float(p / m))
            if total > h:
                l = m + 1
            else:
                k = min(k, m)
                r = m - 1
        return k