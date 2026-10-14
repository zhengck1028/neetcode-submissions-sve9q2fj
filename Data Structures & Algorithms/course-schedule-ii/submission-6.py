class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        graph = defaultdict(list)
        indegree = [0] * numCourses
        res = []
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        while q:
            node = q.popleft()
            res.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        for j in indegree:
            if j > 0:
                return []
        return res