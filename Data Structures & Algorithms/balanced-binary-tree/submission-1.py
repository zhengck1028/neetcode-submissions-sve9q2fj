# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        from collections import deque
        q = deque()
        q.append(root)
        while len(q)>0:
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            if abs(self.getH(cur.left) - self.getH(cur.right)) > 1:
                return False
        
        return True
    
    def getH(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.getH(root.left), self.getH(root.right))