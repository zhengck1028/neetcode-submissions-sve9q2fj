class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            s = strs[i]
            n = len(s)
            res += str(n) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        start = 0
        while i < len(s):
            if s[i] == "#":
                n = int(s[start:i])
                st = s[i+1:i+n+1]
                res.append(st)
                i += n + 1
                start = i
            else:
                i += 1
        return res
