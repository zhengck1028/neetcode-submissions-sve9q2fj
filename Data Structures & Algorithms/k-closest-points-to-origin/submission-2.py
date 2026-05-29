class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, [-math.sqrt(x**2+y**2),[x,y]])
            if len(heap)>k:
                heapq.heappop(heap)
        res = []
        for _, p in heap:
            res.append(p)
        return res