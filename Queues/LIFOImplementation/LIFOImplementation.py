class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack is not None:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        if self.stack is not None:
            return min(self.stack)
        else:
            return None