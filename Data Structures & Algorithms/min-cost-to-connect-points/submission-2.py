class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]
                d = abs(xi-xj)+abs(yi-yj)
                graph[i].append((j, d))
                graph[j].append((i, d))
        heap = [(0, 0)] # (w, v)
        visited = set()
        total = 0
        while heap:
            c, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            total += c
            for v, w in graph[u]:
                if v not in visited:
                    heapq.heappush(heap, (w, v))
        return total

        