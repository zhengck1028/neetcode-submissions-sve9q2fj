class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.comp = n

    def find(self, u):
        if self.root[u] != u:
            self.root[u] = self.find(self.root[u])
        return self.root[u]
    
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU != rootV:
            self.root[rootU] = rootV
            self.comp -= 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u,v)
        return uf.comp