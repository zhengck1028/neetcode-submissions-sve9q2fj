# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        cur = head

        # while nodes[-1] != cur.next:
        #     tail = nodes.pop()
        #     cur.next = tail
        #     cur = cur.next
        #     tail.next = cur

        l, r = 0, len(nodes)-1
        while l<r:
            nodes[l].next = nodes[r]
            if l+1 == r:
                break
            else:
                nodes[r].next = nodes[l+1]
                l +=1
                r-=1
        nodes[r].next = None

        
        
            