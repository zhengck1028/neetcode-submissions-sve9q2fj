class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y = heapq.heappop(heap) * -1
            x = heapq.heappop(heap) * -1
            if y>x:
                y = y - x
                heapq.heappush(heap, -y)
        return -heap[0] if heap else 0
