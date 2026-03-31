class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # [1,0,6], [2,2,6], [2,4,6]
        res = [] # [7,0,1], [7,2,3]
        for i, h in enumerate(heights): # 
            H = h
            L = i
            R = i+1
            if i == 0:
                stack.append([H, L, R])
                continue
            for j in range(len(stack)-1, -1, -1):
                if stack[j][0] > h:
                    L = stack[j][1]
                    prev = stack.pop()
                    res.append(prev)
                else:
                    stack[j][2] = R
            stack.append([H, L, R])
        res = res + stack
        maxA = 0
        for h, l, r in res:
            A = h*(r-l)
            maxA = max(maxA, A)
        return maxA
