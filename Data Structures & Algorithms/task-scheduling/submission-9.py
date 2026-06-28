class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashMap = Counter(tasks)
        availList = [] # (-frequency, task) maxHeap
        waitList = collections.deque() # (time, frequency, task)
        for k, v in hashMap.items():
            heapq.heappush(availList, (-v ,k))
        time = 0
        while waitList or availList:
            time += 1
            while waitList and waitList[0][0] <= time:
                _, frequency, task = waitList.popleft()
                heapq.heappush(availList, (-frequency, task))
            if availList:
                f, t = heapq.heappop(availList)
                f += 1
                next_time = time + n + 1
                if f < 0:
                    waitList.append((next_time, -f, t))
        return time                

