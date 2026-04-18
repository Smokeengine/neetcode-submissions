class MinStack:

    def __init__(self):
        self.stack =[]
        self.min_stk = []
        

    def push(self, val: int) -> None:
        if self.min_stk:
            self.min_stk.append(min(val,self.min_stk[-1]))

        else:
            self.min_stk.append(val)
        self.stack.append(val)
        

    def pop(self) -> None:
        if self.stack:
            self.min_stk.pop()
            self.stack.pop()


        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stk[-1]

        
