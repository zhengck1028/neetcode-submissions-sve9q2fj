# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        def dfs(root):
            nonlocal res
            left = dfs(root.left) if root.left else 0
            right = dfs(root.right) if root.right else 0
            res = max(res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return res