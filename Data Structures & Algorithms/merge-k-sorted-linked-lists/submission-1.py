# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new = cur = ListNode()
        
        while True:
            minNode = ListNode(1001)
            idx = 1001
            for i, h in enumerate(lists):
                if not h:
                    continue
                if h.val < minNode.val:
                    minNode = h
                    idx = i
            if minNode.val == 1001:
                break
            cur.next = minNode
            lists[idx] = lists[idx].next
            cur = cur.next
        return new.next