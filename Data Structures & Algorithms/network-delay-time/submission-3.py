class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v ,w in times:
            graph[u].append((v, w))
        minHeap = [(0, k)]
        t = 0
        visit = set()
        while minHeap:
            w, u = heapq.heappop(minHeap)
            if u in visit:
                continue
            visit.add(u)
            t = w
            for v, w1 in graph[u]:
                if v not in visit:
                    heapq.heappush(minHeap, (w + w1, v))

        return t if len(visit) == n else -1