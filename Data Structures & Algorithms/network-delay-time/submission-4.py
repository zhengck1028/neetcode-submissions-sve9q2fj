class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        res = 0
        visit = set()
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append([v, t]) # [target, time]
        minHeap = [[0, k]]
        while minHeap:
            t, u = heapq.heappop(minHeap)
            if u in visit:
                continue
            visit.add(u)
            res = t
            for nei, ti in graph[u]:
                if nei not in visit:
                    heapq.heappush(minHeap, [t + ti, nei])
        return res if len(visit)== n else -1