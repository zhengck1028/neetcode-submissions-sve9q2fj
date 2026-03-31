class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]
        res = 0
        while l < r:
            maxLeft = max(maxLeft, height[l])
            maxRight = max(maxRight, height[r])
            
            if maxLeft < maxRight:
                res += maxLeft - height[l]
                l += 1
            else:
                res += maxRight - height[r]
                r -= 1
        return res