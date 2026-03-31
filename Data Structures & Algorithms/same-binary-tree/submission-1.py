# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queq = collections.deque()
        queq.append([p,q])

        while queq:
            for i in range(len(queq)):
                node = queq.pop()
                if node[0] and node[1]:
                    if node[0].val == node[1].val:
                        queq.append([node[0].left, node[1].left])
                        queq.append([node[0].right, node[1].right])
                    else:
                        return False
                elif node[0] and not node[1]:
                    return False
                elif node[1] and not node[0]:
                    return False
        
        return True