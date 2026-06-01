class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] += 1
        res = []
        q = deque([i for i, v in enumerate(indegree) if v == 0])
        while q:
            for i in range(len(q)):
                pre = q.popleft()
                res.append(pre)
                for crs in graph[pre]:
                    indegree[crs] -= 1
                    if indegree[crs] == 0:
                        q.append(crs)
        for i in indegree:
            if i > 0:
                return []
        return res