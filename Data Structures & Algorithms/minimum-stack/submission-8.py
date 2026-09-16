class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_ or val <= self.min_[-1]:
            self.min_.append(val)

    def pop(self) -> None:
        curr = self.stack.pop()
        if curr == self.min_[-1]:
            self.min_.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_[-1]
