class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = ["0"]*len(temperatures)
        for L in range(len(temperatures)):
            for R in range(L+1, len(temperatures)):
                if temperatures[R] > temperatures[L]:
                    res[L] = R - L
                    break
        
        return res
