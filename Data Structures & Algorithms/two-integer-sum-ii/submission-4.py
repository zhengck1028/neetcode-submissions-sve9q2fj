class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(numbers):
            hashMap[num] = i + 1
            
        for num in hashMap:
            if target - num in hashMap:
                return [hashMap[num], hashMap[target - num]]