class MinStack:

    def __init__(self):
        self.stack = []
        self.extra = []   

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.extra[-1] if self.extra else val)
        self.extra.append(val)        

    def pop(self) -> None:
        self.extra.pop()
        self.stack.pop()
        
    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        
    def getMin(self) -> int:
        return self.extra[-1]        
