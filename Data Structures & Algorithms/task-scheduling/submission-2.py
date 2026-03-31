class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        hm = {}
        for t in tasks:
            hm[t] = hm.get(t, 0) +1
        maxheap = [-x for x in hm.values()]
        heapq.heapify(maxheap)
        q = deque()

        while maxheap or q:
            time += 1
            if maxheap:
                a = heapq.heappop(maxheap) + 1
                if a < 0:
                    q.append([a, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])

        return time