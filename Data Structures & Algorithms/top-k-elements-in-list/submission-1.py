class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #2.4
        hm = defaultdict(int)
        for i in nums:
            hm[i] += 1
        res = sorted(hm.values(),reverse=True)[:k]
        ress = []
        for k, v in hm.items():
            if v in res:
                ress.append(k)
        return ress
        