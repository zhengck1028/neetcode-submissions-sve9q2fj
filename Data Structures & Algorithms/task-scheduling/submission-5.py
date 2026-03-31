class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        avail_heap = [] # [-count,  val]
        wait_heap = [] # [min_next, -count,  val]
        hm = Counter(tasks)
        for k ,v in hm.items():
            heapq.heappush(avail_heap, [-1 * v, k])
        while avail_heap or wait_heap:
            time += 1
            while wait_heap and wait_heap[0][0] == time:
                time, count, val = heapq.heappop(wait_heap)
                heapq.heappush(avail_heap, [count, val])
            if avail_heap:
                count, val = heapq.heappop(avail_heap)
                count += 1
                if count < 0:
                    heapq.heappush(wait_heap, [time + n + 1, count, val])
        return time
        