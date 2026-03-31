class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        n = len(gas)
        left = []
        for i in range(n):
            left.append(gas[i] - cost[i])
        
        for i in range(n):
            if left[i]>=0:
                tank = 0
                j = i
                while j < i + n:
                    tank += left[j % n]
                    j += 1
                    if tank < 0:
                        break
                if j % n == i:
                    return i
        return -1
