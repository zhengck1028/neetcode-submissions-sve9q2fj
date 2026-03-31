# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = 1
        depth_left = depth + (self.maxDepth(root.left) if root.left else 0)
        depth_right = depth + (self.maxDepth(root.right) if root.right else 0)
        depth = max(depth_left, depth_right)
        return depth