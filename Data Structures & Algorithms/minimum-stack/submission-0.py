class MinStack:

    def __init__(self):
        self.stack = []
        self.min_ = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_:
            self.min_.append(min(val, self.min_[-1]))
        else:
            self.min_.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.min_[-1]
