class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        cur_prod = 1
        res = 0
        for r in range(len(nums)):
            cur_prod *= nums[r]
            while l<=r and cur_prod >= k:
                cur_prod //= nums[l]
                l += 1
            res += (r - l + 1)
            # l = 0, r = 2
            # [10, 5, 2]
            # [10, 5, 2], [5, 2], [2] # 3 possiblities = length
        return res