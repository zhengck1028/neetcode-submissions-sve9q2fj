class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UF(n)
        for u, v in edges:
            uf.union(u, v)
        return uf.comps

class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.comps = n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU != rootV:
            self.comps -= 1
            self.parent[rootU] = rootV
