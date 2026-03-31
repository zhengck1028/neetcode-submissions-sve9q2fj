class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_amt = 0
        
        while l<r:
            amt = (r-l)*min(heights[l], heights[r])
            if amt>max_amt:
                max_amt = max(amt, max_amt)
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return max_amt
