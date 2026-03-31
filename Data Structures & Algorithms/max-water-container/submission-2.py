class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        l, r = 0, len(heights) - 1
        res = 0
        while l <= r:
            A = min(heights[l], heights[r]) * (r - l)
            res = max(res, A)
            if heights[l] <=  heights[r]:
                l += 1
            else:
                r -= 1
        return res