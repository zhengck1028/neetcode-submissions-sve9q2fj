class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        visited = set()
        for a, b in prerequisites:
            graph[a].append(b)
        def dfs(i):
            if i in visited:
                return False
            visited.add(i)
            for pre in graph[i]:
                if not dfs(pre):
                    return False
            visited.remove(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True