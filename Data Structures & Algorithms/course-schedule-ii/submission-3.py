class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        res = []
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        q = deque([n for n in range(numCourses) if in_degree[n] == 0])
        while q:
            node = q.popleft()
            res.append(node)
            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        return res if len(res) == numCourses else []