# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        plus1 = 0
        res = ListNode()
        cur = res
        while cur1 or cur2:
            a = cur1.val if cur1 else 0
            b = cur2.val if cur2 else 0
            sum_ = a + b + plus1
            plus1 = 0
            if sum_ >= 10:
                sum_ = sum_ -10
                plus1 = 1
            cur.val = sum_
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
            if cur1 or cur2:
                cur.next = ListNode()
                cur = cur.next
        if plus1 ==1:
            cur.next = ListNode(1)
        return res
