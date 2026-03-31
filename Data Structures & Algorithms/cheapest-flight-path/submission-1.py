class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, p in flights:
            graph[s].append((d, p))
        min_stops = {i: float('inf') for i in range(n)}
        minHeap = [[0, src, -1]]
        while minHeap:
            price, u, kk = heapq.heappop(minHeap)
            if u == dst:
                return price
            if kk > k or kk >= min_stops[u]:
                continue
            min_stops[u] = kk
            
            for v ,w in graph[u]:
                if kk < k:
                    heapq.heappush(minHeap, [price + w, v, kk+1])
        return -1
