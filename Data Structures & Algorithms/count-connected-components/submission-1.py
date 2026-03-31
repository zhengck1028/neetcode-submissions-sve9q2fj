class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visit = set()
        res = 0
        def dfs(i, par):
            if i in visit:
                return
            visit.add(i)
            for j in graph[i]:
                if j == par:
                    continue
                dfs(j, i)
            return
        
        for i in range(n):
            if i not in visit:
                dfs(i, -1)
                res += 1
        return res