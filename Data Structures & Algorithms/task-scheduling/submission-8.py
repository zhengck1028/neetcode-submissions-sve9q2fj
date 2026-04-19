class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = Counter(tasks)
        avail = [] # maxheap, [-count]
        wait = deque() # queue, [next_time, remaining]
        for k, v in hm.items():
            heapq.heappush(avail, -v)
        time = 0
        while avail or wait:
            time += 1
            while wait and wait[0][0] <= time:
                _, remaining = wait.popleft()
                heapq.heappush(avail, remaining)
            if avail:
                count = heapq.heappop(avail)
                next_time = time + n + 1
                count += 1
                if count < 0:
                    wait.append([next_time, count])
        return time