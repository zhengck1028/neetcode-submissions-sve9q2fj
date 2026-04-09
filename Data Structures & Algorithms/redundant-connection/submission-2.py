class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UF(n)
        for u, v in edges:
            if uf.union(u-1,v-1):
                return [u, v]

class UF:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU != rootV:
            self.parent[rootU] = rootV
            return False
        else:
            return True