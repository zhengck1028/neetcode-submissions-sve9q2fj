# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, maxV, minV):
            if not root:
                return True
            if minV < root.val < maxV:
                return dfs(root.left, root.val, minV) and dfs(root.right, maxV, root.val)
            else:
                return False
        return dfs(root, float("inf"), float("-inf"))