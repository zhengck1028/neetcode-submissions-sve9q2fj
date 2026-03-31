# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque
        if not root:
            return root

        q = deque()
        q.append(root)

        while q:
            cur = q.popleft()
            tmp = cur.left
            cur.left=cur.right
            cur.right=tmp
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            
        return root