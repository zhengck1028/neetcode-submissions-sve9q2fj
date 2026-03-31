# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        cur = head
        prev = None
        # reverse 
        while cur:
            tmp = cur.next
            cur.next=prev
            prev=cur
            cur=tmp
        # remove nth node 
        cur = tail = prev
        prev = None
        cnt = 1
        while cur and cnt < n:
            prev=cur
            cur=cur.next
            cnt += 1
        if n == 1:
            tail = tail.next
        else:
            prev.next=cur.next
        
        # reverse again
        cur = tail
        prev = None
        # reverse 
        while cur:
            tmp = cur.next
            cur.next=prev
            prev=cur
            cur=tmp
        return prev