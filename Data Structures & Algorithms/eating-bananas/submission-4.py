class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_p = max(piles)
        L, R = 1, max_p
        res = max_p
        while L <= R:
            M = (L + R) // 2
            hr = 0
            for i in range(len(piles)):
                hr += math.ceil(float(piles[i])/M)
            if hr <= h:
                res = M
                R = M - 1
            elif hr > h:
                L = M + 1
        return res

