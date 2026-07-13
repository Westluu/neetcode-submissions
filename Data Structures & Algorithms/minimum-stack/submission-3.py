class MinStack:

    def __init__(self):
        self.stack = []
        self.cur_min = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.cur_min = val
        else:
            prev_min = self.stack[-1][1]
            self.cur_min = min(val, prev_min)
        self.stack.append((val, self.cur_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]  

    def getMin(self) -> int:
        return self.stack[-1][1]
        
