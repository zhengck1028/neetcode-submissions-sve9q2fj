# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hm = {}
        i = 0
        while head and head.next:
            hm[head] = i
            if head.next in hm:
                return True
            head = head.next
        return False