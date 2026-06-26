# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prv = None
        # sec -> [4,5,6]
        cur = slow.next
        slow.next = None
        while cur:
            tmp = cur.next
            cur.next = prv
            prv, cur = cur, tmp
        
        second = prv
        first = head
        # first [0, 1, 2, 3]
        # second [6, 5, 4]
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2