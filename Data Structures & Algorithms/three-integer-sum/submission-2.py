class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, f in enumerate(nums):
            if f > 0: # 因为已排序，如果第一个大于0，可以终止循环了
                break
            if i>0 and f == nums[i-1]:
                continue
            l, r = i +1, len(nums) - 1
            while l<r:
                threeSum = f + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([f, nums[l], nums[r]])
                    l += 1 # 不要忘了还有更多可能组合， 继续探索
                    r -= 1
                    while nums[l] == nums[l-1] and l<r: # 跳过重复
                        l += 1
                    while nums[r] == nums[r+1] and l<r: # 跳过重复
                        r -= 1
        return res