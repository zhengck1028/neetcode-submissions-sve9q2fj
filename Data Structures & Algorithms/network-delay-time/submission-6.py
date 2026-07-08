class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        dist = [float("inf")] * (n + 1)
        minHeap = [(0, k)]
        dist[k] = 0
        while minHeap:
            t, u = heapq.heappop(minHeap)
            if dist[u] < t:
                continue
            for v, w in graph[u]:
                newT = t + w
                if dist[v] > newT:
                    dist[v] = newT
                    heapq.heappush(minHeap, (newT, v))
        res = max(dist[1:])
        return res if res < float("inf") else -1