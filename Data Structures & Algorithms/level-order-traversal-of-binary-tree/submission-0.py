# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BST
        res = []
        from collections import deque
        level = 0
        q = deque()
        q.append(root)
        while len(q)>0:
            for a in range(len(q)):
                cur = q.popleft()
                if cur:
                    q.append(cur.left)
                    q.append(cur.right)
                    try:
                        res[level].append(cur.val)
                    except:
                        res.append([cur.val])
            level += 1
        return res