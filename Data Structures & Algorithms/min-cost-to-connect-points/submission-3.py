class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                if i == j:
                    continue
                x1, y1 = p1[0], p1[1]
                x2, y2 = p2[0], p2[1]
                dist = abs(x1-x2) + abs(y1-y2)
                edges.append([i, j, dist])
        res = 0
        n = len(points)
        uf = UF(n)
        edges_used = 0
        edges.sort(key=lambda x: x[2])
        for i, j, cost in edges:
            if uf.union(i, j):
                res += cost
                edges_used += 1
                if edges_used == n-1:
                    break
        return res

class UF:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]

    def  find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            self.parent[root_u] = self.parent[v]
            return True
        return False