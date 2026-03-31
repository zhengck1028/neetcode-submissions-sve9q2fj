class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n+1)]
        def find(i):
            if parents[i] != i:
                parents[i] = find(parents[i])
            return parents[i]
        
        def union(i, j):
            pi = find(i)
            pj = find(j)
            if pi == pj:
                return False
            parents[pi]= pj
            return True

        for a, b in edges:
            if not union(a,b):
                return [a, b]