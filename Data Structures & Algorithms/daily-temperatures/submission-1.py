class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack method
        res = ["0"]*len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                tempID, temp = stack.pop()
                res[tempID] = i - tempID
            stack.append((i, t))
        return res