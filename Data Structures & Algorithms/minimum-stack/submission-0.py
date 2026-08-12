class MinStack:

    def __init__(self):
        self.stack = list()
        self.min_stack = list()
        self.min_stack.append(float('inf'))

    def push(self, val: int) -> None:
        self.min_stack.append(min(self.min_stack[-1], val))
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
