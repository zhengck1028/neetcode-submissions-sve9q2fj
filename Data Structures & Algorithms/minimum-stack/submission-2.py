class MinStack:

    def __init__(self):
        self.stack = []
        self.min_= []

    def push(self, val: int) -> None:
        self.min_.append(min(self.min_[-1], val) if self.min_ else val)
        self.stack.append(val)

    def pop(self) -> None:
        self.min_.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_[-1]
        
