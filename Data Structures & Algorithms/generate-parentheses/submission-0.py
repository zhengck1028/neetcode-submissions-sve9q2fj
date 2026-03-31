class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curSet = []
        def dfs(curSet, left, right):
            if left == n and right == n:
                res.append(''.join(curSet))
                return
            if left < n:
                curSet.append("(")
                dfs(curSet, left+1, right)
                curSet.pop()
            if left > right:
                curSet.append(")")
                dfs(curSet, left, right + 1)
                curSet.pop()
        dfs(curSet, 0, 0)
        return res
            
