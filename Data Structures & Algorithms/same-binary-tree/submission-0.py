# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. 两个都为空：说明目前为止结构和值都一样（或者都遍历完了）
        if not p and not q:
            return True
        
        # 2. 一个为空，另一个不为空：结构不一样
        if not p or not q:
            return False
            
        # 3. 两个都不为空，但值不一样
        if p.val != q.val:
            return False
        
        # 4. 当前节点没问题，继续递归检查左右子树
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
