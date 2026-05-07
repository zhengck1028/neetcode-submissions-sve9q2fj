# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        def dfs(node):
            if not node:
                return False
            if node.val == subRoot.val and self.isSameTree(node, subRoot):
                return True
            else:
                return dfs(node.left) or dfs(node.right)
        return dfs(root)


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            elif node1 and node2:
                if node1.val != node2.val:
                    return False
                else:
                    return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
            else:
                return False
        return dfs(p, q)