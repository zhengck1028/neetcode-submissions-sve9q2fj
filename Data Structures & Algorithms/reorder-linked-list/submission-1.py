# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        sec = slow.next
        prev = slow.next = None

        while sec:
            tmp = sec.next
            sec.next = prev
            prev = sec
            sec = tmp

        sec = prev
        fis = head
        while sec:
            tmp1 = fis.next
            tmp2 = sec.next
            fis.next=sec
            sec.next=tmp1
            fis=tmp1
            sec=tmp2
            
