# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid node
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # break
        second = slow.next
        slow.next = None
        # reverse the second list
        prv = None
        cur = second
        while cur:
            tmp = cur.next
            cur.next = prv
            prv = cur
            cur = tmp
        # merge two lists
        first = head
        second = prv
        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next, second.next = second, tmp1
            first, second = tmp1, tmp2


