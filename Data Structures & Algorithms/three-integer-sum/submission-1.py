class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hmap = dict()
        res = []
        hm_nums = {}
        for i in range(len(nums)):
            if nums[i] in hm_nums:
                hm_nums[nums[i]].append(i)
            else:
                hm_nums[nums[i]] = [i]

        for i in range(len(nums)):
            for j in range(len(nums)-1, -1, -1):
                if i == j:
                    continue
                sum_ = nums[i] + nums[j]
                if -sum_ in hm_nums:
                    if set([i, j]) & set(hm_nums[-sum_]) != set(hm_nums[-sum_]):
                        r = sorted([nums[i], nums[j], -sum_])
                        if r not in res:
                            res.append(r)
        return res