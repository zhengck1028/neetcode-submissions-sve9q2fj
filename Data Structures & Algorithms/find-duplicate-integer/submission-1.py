class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        n = len(nums)
        while True:
            a = nums[slow % n]
            b = nums[fast % n]
            if a == b and slow>0:
                return a
            else:
                slow += 1
                fast += 2