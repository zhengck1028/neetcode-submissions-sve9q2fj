class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        avail_heap = []
        wait_heap = []
        counter = Counter(tasks)
        for t, c in counter.items():
            heapq.heappush(avail_heap, [-c, t])
        while avail_heap or wait_heap:
            time += 1
            while wait_heap and wait_heap[0][0] <= time:
                _, c, t = heapq.heappop(wait_heap)
                heapq.heappush(avail_heap, [c, t])
            if avail_heap:
                count, task = heapq.heappop(avail_heap)
                count += 1
                if count < 0:
                    heapq.heappush(wait_heap, [time + n + 1, count, task])
        return time