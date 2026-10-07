class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse= True)
        stack = []
        for pos, spd in cars:
            curT = (target - pos) / spd
            if not stack or curT > stack[-1]:
                stack.append(curT)
        return len(stack)