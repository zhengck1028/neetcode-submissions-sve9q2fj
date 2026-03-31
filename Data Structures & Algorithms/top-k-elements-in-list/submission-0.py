class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for n in set(nums):
            count[n] = sum([x==n for x in nums])
        c = sorted(list(count.values()), reverse=True)
        c = c[:k]
        output = []
        for ke, v in count.items():
            if v in c:
                output.append(ke)
        return output