class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps={")":"(","}":"{","]":"["}
        for ss in s:
            if ss in maps.keys():
                if stack and stack[-1] == maps[ss]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ss)
        if stack:
            return False
        else:
            return True