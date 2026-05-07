class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            "2" : ("a", "b", "c"),
            "3" : ("d", "e", "f"),
            "4" : ("g", "h", "i"),
            "5" : ("j", "k", "l"),
            "6" : ("m", "n", "o"),
            "7" : ("p", "q", "r", "s"),
            "8" : ("t", "u", "v"),
            "9" : ("w", "x", "y", "z")
        }
        res = []
        def dfs(i, curSet):
            if i == len(digits):
                res.append("".join(curSet))
                return
            for s in mapping[digits[i]]:
                curSet.append(s)
                dfs(i+1, curSet)
                curSet.pop()
        dfs(0, [])
        return res