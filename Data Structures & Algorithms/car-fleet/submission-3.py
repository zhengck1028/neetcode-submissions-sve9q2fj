class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(x,y) for x, y in zip(position, speed)]
        pair = sorted(pair, reverse=True)
        stack = []
        for p, s in pair:
            t = (target - p)/s
            stack.append((p, s, t))
            if len(stack)>=2 and t<= stack[-2][2]:
                stack.pop()
            
        return len(stack)