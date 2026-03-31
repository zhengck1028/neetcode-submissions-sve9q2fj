class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            j = i + 1
            while j < len(numbers):
                if numbers[j] == target - numbers[i]:
                    return [i+1, j+1]
                else:
                    j += 1