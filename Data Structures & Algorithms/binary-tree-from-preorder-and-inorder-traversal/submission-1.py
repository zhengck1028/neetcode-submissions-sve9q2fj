# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root_v = preorder[0]
        k = inorder.index(root_v)
        prleft = preorder[1:k+1]
        prright = preorder[k+1:]
        inleft = inorder[:k]
        inright = inorder[k+1:]
        root = TreeNode(root_v)
        root.left = self.buildTree(prleft,inleft)
        root.right = self.buildTree(prright,inright)
        return root