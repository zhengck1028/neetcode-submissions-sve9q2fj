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
        new = Node(0)
        newhead = new
        cur = head
        hm = {None: None}
        while cur:
            new.val = cur.val
            new.next = Node(0) if cur.next else None
            new.random = cur.random
            hm[cur] = new
            cur = cur.next
            new = new.next
        new = newhead
        while new:
            new.random = hm[new.random]
            new = new.next
        return newhead