# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return
            if min(p.val, q.val) <= node.val <= max(p.val, q.val):
                return node
            elif node.val < min(p.val, q.val):
                return dfs(node.right)
            else:
                return dfs(node.left)
        return dfs(root)