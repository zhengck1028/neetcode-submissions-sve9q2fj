class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        visited = set()
        completed = set()
        for a, b in prerequisites:
            graph[a].append(b)
        res = []
        def dfs(i):
            if i in visited:
                return False
            if i in completed:
                return True
            visited.add(i)
            for pre in graph[i]:
                if not dfs(pre):
                    return False
            visited.remove(i)
            completed.add(i)
            res.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res