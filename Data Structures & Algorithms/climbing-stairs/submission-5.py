class Solution:
    def climbStairs(self, n: int) -> int:
        prv2, prv1 = 1, 1
        for i in range(2, n+1):
            cur = prv1 + prv2
            prv2 = prv1
            prv1 = cur
        return prv1