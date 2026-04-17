from collections import defaultdict, deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {ch: set() for word in words for ch in word}
        indegree = {ch: 0 for word in words for ch in word}

        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]

            # invalid case: prefix conflict
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        q = deque([ch for ch in indegree if indegree[ch] == 0])
        res = []

        while q:
            ch = q.popleft()
            res.append(ch)

            for nei in graph[ch]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return "".join(res) if len(res) == len(indegree) else ""