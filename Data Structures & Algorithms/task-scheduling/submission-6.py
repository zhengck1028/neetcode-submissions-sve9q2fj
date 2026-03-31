class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        hashMap = Counter(tasks)
        maxHeap = []
        minHeap = []
        for k, v in hashMap.items():
            heapq.heappush(maxHeap, [-v, k])
        
        while maxHeap or minHeap:
            
            while minHeap and time >= minHeap[0][0]:
                _, v, k = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, [v, k])
            if maxHeap:
                v, k = heapq.heappop(maxHeap)
                v = v + 1
                if v:
                    nextAvail = time + n + 1
                    heapq.heappush(minHeap, [nextAvail, v, k])
            time += 1
        return time