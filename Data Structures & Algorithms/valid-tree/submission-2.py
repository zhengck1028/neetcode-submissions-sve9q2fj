class UF:
    def __init__(self, n) -> None:
        self.parent = list(range(n+1))
        self.comps = n
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        self.comps -= 1
        self.parent[pu] = pv
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UF(n)
        for u, v in edges:
            if not uf.union(u, v):
                return False
        return uf.comps == 1