"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        newhead = Node(0)
        cur = head
        newcur = newhead
        random = []
        hm = {}
        while cur:
            newcur.val = cur.val
            newcur.next = Node(0) if cur.next else None
            random.append(cur.random)
            hm[cur] = newcur
            newcur= newcur.next
            cur = cur.next
        newcur = newhead
        for i in range(len(random)):
            if random[i]:
                random[i] = hm[random[i]]
            newcur.random = random[i]
            newcur = newcur.next
        return newhead
