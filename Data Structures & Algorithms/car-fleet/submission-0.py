class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(x,y) for x,y in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            t = (target - p) /s
            stack.append(t)
            if  1 and len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack)

