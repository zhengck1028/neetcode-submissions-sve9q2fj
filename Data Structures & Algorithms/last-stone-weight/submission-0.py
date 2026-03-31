class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)
        while len(maxheap)>=2:
            y = heapq.heappop(maxheap) * -1
            x = heapq.heappop(maxheap) * -1
            if x < y:
                y = y - x
                heapq.heappush(maxheap, y* -1)
        if not maxheap:
            return 0
        else:
            return maxheap[0] * -1
