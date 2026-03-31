class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = {}
        for t in tasks:
            hm[t] = hm.get(t, 0) + 1
        k = max(hm.values())
        m = 0
        for key, value in hm.items():
            if value == k:
                m += 1
        L = len(tasks)
        return k + max(n*(k-1) + m - 1, L-k)