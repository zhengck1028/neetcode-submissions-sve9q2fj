# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxV):
            if not root:
                return 0
            cnt = 1 if root.val >= maxV else 0
            maxV = max(root.val, maxV)
            cnt = cnt + dfs(root.left, maxV)
            cnt = cnt + dfs(root.right, maxV)
            return cnt
        return dfs(root, root.val)