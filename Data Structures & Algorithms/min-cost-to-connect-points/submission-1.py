class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph= defaultdict(list)
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                graph[i].append((j, abs(p1[0]-p2[0])+abs(p1[1]-p2[1])))
                # graph[j].append((i, abs(p1[0]-p2[0])+abs(p1[1]-p2[1])))
        visit =set()
        minHeap = [[0, graph[0][0][0]]]
        res = 0
        while minHeap:
            curDist, u = heapq.heappop(minHeap)
            if u in visit:
                continue
            visit.add(u)
            res += curDist
            for v, w in graph[u]:
                if v not in visit:
                    heapq.heappush(minHeap, [w, v])
        
        return res

        