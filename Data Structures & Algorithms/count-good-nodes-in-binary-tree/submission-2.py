# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, maxV):
            if not node:
                return
            nonlocal res
            if node.val >= maxV:
                res += 1
            maxV = max(maxV, node.val)
            dfs(node.left, maxV)
            dfs(node.right, maxV)
        
        dfs(root, float("-inf"))
        return res