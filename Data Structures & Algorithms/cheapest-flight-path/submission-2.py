from collections import deque, defaultdict
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 1. 建图
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
            
        # 2. 维护到达每个城市的历史最低价，初始为无限大
        prices = [float('inf')] * n
        prices[src] = 0
        
        # 3. BFS 队列，存的是：(当前城市, 到达这里的累计花费)
        q = deque([(src, 0)])
        stops = 0
        
        # 4. 像水波纹一样按层扩散，最多扩散 k + 1 层
        while q and stops <= k:
            size = len(q)
            
            # 一次性把当前这一层（这一站）的所有路线全走完
            for _ in range(size):
                u, cost = q.popleft()
                
                # 遍历下一站能飞去哪
                for v, w in graph[u]:
                    new_cost = cost + w
                    
                    # 💡 核心剪枝：只有当这条新路线比以前飞到 v 的路线更便宜时，才值得继续探索！
                    if new_cost < prices[v]:
                        prices[v] = new_cost
                        q.append((v, new_cost))
            
            # 走完一层，转机次数 + 1
            stops += 1
            
        return prices[dst] if prices[dst] != float('inf') else -1