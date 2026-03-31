class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0]*numCourses 
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
            in_degree[b] += 1
        
        q = deque([i for i, v in enumerate(in_degree) if v == 0])
        res = []
        finished = 0
        while q:
            cr = q.popleft()
            res.append(cr)
            finished += 1
            for pr in graph[cr]:
                in_degree[pr] -= 1
                if in_degree[pr] == 0:
                    q.append(pr)
        res.reverse()
        return res if finished == numCourses else []