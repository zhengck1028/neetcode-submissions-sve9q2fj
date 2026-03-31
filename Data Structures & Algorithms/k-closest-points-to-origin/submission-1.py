class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            x, y = p[0], p[1]
            dst = (x*x+y*y)**0.5
            heapq.heappush(heap, [-dst,[x,y]])
            if len(heap)>k:
                heapq.heappop(heap)
        return [p for d,p in heap]