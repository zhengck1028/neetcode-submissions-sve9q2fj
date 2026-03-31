class Solution:
    def jump(self, nums: List[int]) -> int:
        cnt = 0
        
        R = len(nums) -1
        while R > 0:
            L = R - 1
            maxjump = [L, 0]
            while L >= 0:
                if nums[L] >= (R - L) and nums[L] > maxjump[1]:
                    maxjump[0] = L
                    maxjump[1] = R - L
                L -= 1
            R = maxjump[0]
            cnt += 1
        return cnt