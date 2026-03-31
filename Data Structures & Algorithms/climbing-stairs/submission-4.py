class Solution:
    def climbStairs(self, n: int) -> int:
        prv1 = 1
        prv2 = 1
        for i in range(2, n+1):
            cur = prv1+prv2
            prv1 = prv2
            prv2 = cur
        return prv2