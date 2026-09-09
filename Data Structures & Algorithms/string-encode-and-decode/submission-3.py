class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = len(s)
            res += str(l) + "#" + s
        return res 
        
    # 5#hello5#world
    def decode(self, s: str) -> List[str]:
        res = []
        i = j = 0
        while i < len(s):
            ss = s[j]
            if ss != "#":
                j += 1
            else:
                l = s[i:j]
                l = int(l)
                i = j + l + 1
                res.append(s[j+1:j + l + 1])
                j = i
        return res