class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if stack:
                left = stack[-1]
                if (ch == "}" and left == "{") or \
                (ch == ")" and left == "(") or \
                (ch == "]" and left == "[") :
                    stack.pop()
                    continue
            stack.append(ch)
        return not stack
                