class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))
        distances = [[float("inf")] * (k + 2) for _ in range(n)]
        minHeap = [(0, src, -1)] # (cost, destination, stops)
        distances[src][0] = 0
        while minHeap:
            cost, start, stops = heapq.heappop(minHeap)
            if start == dst:
                return cost
            if stops == k or distances[start][stops + 1] < cost:
                continue
            
            for end, p in graph[start]:
                nextCost = cost + p
                nextStops = stops + 1
                if distances[end][nextStops + 1] > nextCost:
                    distances[end][nextStops + 1] = nextCost
                    heapq.heappush(minHeap, (nextCost, end, nextStops))
        return -1