class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v ,w in times:
            graph[u].append((v, w))
        heap = [(0, k)]
        t = 0
        visit = set()
        while heap:
            w, u = heapq.heappop(heap)
            if u in visit:
                continue
            visit.add(u)
            t = w
            for v ,wi in graph[u]:
                if v not in visit:
                    heapq.heappush(heap, (w+wi, v))
        return t if len(visit) == n else -1