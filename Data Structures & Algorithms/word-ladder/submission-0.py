from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList.append(beginWord)

        n = len(wordList)
        word_len = len(wordList[0])

        graph = defaultdict(list)

        def one_diff(w1, w2):
            diff = 0
            for i in range(word_len):
                if w1[i] != w2[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1

        for i in range(n):
            for j in range(i + 1, n):
                if one_diff(wordList[i], wordList[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        start = wordList.index(beginWord)
        q = deque([start])
        visit = set([start])
        steps = 1

        while q:
            for _ in range(len(q)):
                idx = q.popleft()

                if wordList[idx] == endWord:
                    return steps

                for nei in graph[idx]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)

            steps += 1

        return 0