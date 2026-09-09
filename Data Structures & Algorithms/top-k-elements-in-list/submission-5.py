class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []  # size k
        counter = Counter(nums)
        for key, val in counter.items():
            heapq.heappush(min_heap, (val, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [key for val, key in min_heap]
