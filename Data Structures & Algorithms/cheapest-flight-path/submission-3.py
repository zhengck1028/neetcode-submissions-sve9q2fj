class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        q = deque([(0, src, 0)])
        price = [float("inf")] * n
        price[src] = 0
        while q:
            for _ in range(len(q)):
                w, u, stops = q.popleft()
                if stops > k:
                    continue
                for v, dw in graph[u]:
                    p = w + dw
                    if p < price[v]:
                        price[v] = p
                        q.append((p, v, stops + 1))
        return price[dst] if price[dst] != float("inf") else -1