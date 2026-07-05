class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        
        minHeap = [(0, k)]
        distances = [float("inf")] * (n + 1) # distances to kth node
        distances[k] = 0

        while minHeap:
            t, u = heapq.heappop(minHeap)

            if t > distances[u]:
                continue
            
            for v, w in graph[u]:
                newDist = t + w
                if newDist < distances[v]:
                    distances[v] = newDist
                    heapq.heappush(minHeap, (newDist, v))
        res = max(distances[1:])
        return res if res < float("inf") else -1
