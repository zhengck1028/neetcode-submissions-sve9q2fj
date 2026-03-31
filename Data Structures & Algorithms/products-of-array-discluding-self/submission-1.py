class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        suff = [1] * len(nums)

        for i in range(1, len(nums)):
            pref[i] = pref[i-1] * nums[i-1]
        for j in range(len(nums)-2, -1, -1):
            suff[j] = suff[j+1] * nums[j+1]

        res = [1] * len(nums)
        for k in range(len(nums)):
            res[k] = pref[k] * suff[k]

        return res