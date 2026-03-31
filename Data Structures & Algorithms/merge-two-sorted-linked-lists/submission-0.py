# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ress = ListNode()
        res = ress
        while list1 or list2:
            if not list1:
                res.next = list2
                break
            if not list2:
                res.next = list1
                break
            if list1.val <= list2.val:
                tmp = list1
                list1 = list1.next
            else:
                tmp = list2
                list2 = list2.next
            res.next = tmp
            tmp.next = None
            res = res.next
        return ress.next