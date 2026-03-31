class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <r:
            m = l + (r-l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        # 0-l-1, l-len(nums)-1
        if target < nums[0] or l == 0:
            # binary search within l-len(nums)-1
            L, R = l, len(nums)-1
        elif  target >= nums[0]:
            # binary search within 0-l-1
            L, R = 0, l - 1
        while L<=R:
            M = L +(R - L) // 2
            if target < nums[M]:
                R = M - 1
            elif target > nums[M]:
                L = M + 1
            else:
                return M
        return -1