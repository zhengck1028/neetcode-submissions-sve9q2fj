class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {")":"(","}":"{","]":"["}
        for ss in s:
            if ss in hm:
                if stack and stack[-1] == hm[ss]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ss)
                

        return False if stack else True