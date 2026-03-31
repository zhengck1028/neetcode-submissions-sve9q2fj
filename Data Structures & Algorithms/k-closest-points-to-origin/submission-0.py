class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            dist = math.sqrt((x)**2 + (y)**2)
            heapq.heappush(minheap,(dist, [x, y]))
        res = []
        while len(res) < k:
            res.append(heapq.heappop(minheap)[1])
        return res