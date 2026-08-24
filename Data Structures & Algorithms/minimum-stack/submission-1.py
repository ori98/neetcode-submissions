class MinStack:

    def __init__(self):
        self.stack = []
        # basically an array to keep track of min element atp
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # at this point, we also capture the min element value atp
        min_val = val
        if self.min_stack:
            if self.min_stack[-1] < val:
                min_val  = self.min_stack[-1]
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]