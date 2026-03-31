# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        cur = head
        while cur:
            N += 1
            cur = cur.next
        cnt = 0
        cur = head
        prev = None
        if N-n == 0:
            return head.next
        while cur:
            cnt += 1
            if cnt == N - n + 1:
                prev.next = cur.next
                cur.next = None
            prev = cur
            cur = cur.next
        return head

