class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        uf = UnionFind(n)
        for u, v in edges:
            if not uf.union(u, v):
                return False
        return True
        
    
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
            return True
        else:
            return False
