class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "*":
                stack.append(c)
            else:
                ast = 0
                usedleft = 0
                while stack:
                    g = stack.pop()
                    if g == "*":
                        ast += 1
                    elif g == "(":
                        usedleft = 1
                        break
                ast = ast - 1 + usedleft
                if ast < 0:
                    return False
                while ast > 0:
                    stack.append("*")
                    ast -= 1
        left = 0
        for i in stack:
            if i == "(":
                left += 1
            elif i == "*":
                left = max(left-1 ,0)

        return left == 0