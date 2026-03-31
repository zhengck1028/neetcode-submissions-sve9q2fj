class Solution:

    def encode(self, strs: List[str]) -> str:
        o = ""
        for w in strs:
            l = len(w)
            o = o + str(l) + "#" + w
        return o

    def decode(self, s: str) -> List[str]:
        l = ""
        i = 0
        res = []
        while i<len(s):
            if s[i] != "#":
                l = l + s[i]
                i+=1
            else:
                l = int(l)
                res.append(s[(i+1):(i+l+1)])
                i = i + l + 1
                l = ""
        return res