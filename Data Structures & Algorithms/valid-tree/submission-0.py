class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False
        graph = {i:[] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visit = set()
        def dfs(i, par):
            if i in visit:
                return False

            visit.add(i)
            for j in graph[i]:
                if j == par:
                    continue
                if not dfs(j, i):
                    return False

            return True
        
        return dfs(0, -1) and len(visit) == n