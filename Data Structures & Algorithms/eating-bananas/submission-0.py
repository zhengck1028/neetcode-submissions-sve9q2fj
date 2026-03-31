class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h: hours limit
        # k: # banana min eating speed
        l, r = 1, max(piles)
        k = h
        while l <= r:
            m = l + (r - l) // 2
            h_cnt = 0
            for b in piles:
                h_cnt += ((b-1) // m ) + 1
            if h_cnt > h:
                l = m + 1
            elif h_cnt <= h:
                r = m - 1
                k = m
        
        return k
