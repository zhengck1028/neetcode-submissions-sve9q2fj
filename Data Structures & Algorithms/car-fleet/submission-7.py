class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, sp) for p, sp in zip(position, speed)]
        cars.sort(reverse= True)
        stack = []
        for pos, spd in cars:
            timeTotarget = (target - pos) / spd
            if not stack or timeTotarget > stack[-1]:
                stack.append(timeTotarget)
        return len(stack)
