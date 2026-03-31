# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, max_v):
            nonlocal res
            if not root:
                return
            if root.val >= max_v:
                res += 1
            max_v = max(max_v, root.val)
            dfs(root.left, max_v)
            dfs(root.right, max_v)
        dfs(root, float("-inf"))
        return res