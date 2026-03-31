class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = s.lower().replace(" ","")
        ss = re.findall(r"[A-Za-z0-9]*", s)
        ss = "".join(ss)
        for l in range(len(ss)//2):
            r = len(ss) - l - 1
            if ss[l] != ss[r]:
                return False
        return True
