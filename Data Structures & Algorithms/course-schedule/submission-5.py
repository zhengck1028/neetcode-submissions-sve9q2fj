class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        for a, b in prerequisites:
            graph[b].append(a) # (0,1) means 1 --> 0
            indegree[a]+=1
        q = deque([i for i, d in enumerate(indegree) if d == 0])
        while q:
            crs = q.popleft()
            for nei in graph[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        for i in indegree:
            if i > 0:
                return False
        return True

