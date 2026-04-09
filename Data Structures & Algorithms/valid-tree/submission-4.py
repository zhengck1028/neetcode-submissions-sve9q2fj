class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        uf = UF(n)
        for u, v in edges:
            if uf.union(u, v):
                return False
        return True
        
    
class UF:
    def __init__(self, n) -> None:
        self.n = n
        self.root = [i for i in range(n)]

    def find(self, node):
        if self.root[node] != node:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU != rootV:
            self.root[rootV] = rootU
        else:
            return True
        return False # cycle
