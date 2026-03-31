class MedianFinder:

    def __init__(self):
        self.max_heap = [] # left half
        self.min_heap = [] # right half

    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -val)
        if len(self.max_heap) < len(self.min_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        odd = (len(self.min_heap) + len(self.max_heap)) % 2
        return -self.max_heap[0] if odd else (-self.max_heap[0]+self.min_heap[0])/2

        