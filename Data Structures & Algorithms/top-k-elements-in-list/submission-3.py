class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = Counter(nums)
        heap = []
        for ke ,va in hm.items():
            heapq.heappush(heap, [va, ke])
            if len(heap) > k:
                heapq.heappop(heap)
        return [k for v, k in heap]
            