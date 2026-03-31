# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow.next
        slow.next = None
        prv = None
        while cur:
            tmp = cur
            cur=cur.next
            tmp.next = prv
            prv = tmp
        
        second = prv

        newHead = ListNode()
        cur = newHead
        while head and second:
            cur.next = head
            head = head.next
            cur = cur.next
            cur.next = second
            second = second.next
            cur = cur.next
        cur.next = head
        head =  newHead.next
