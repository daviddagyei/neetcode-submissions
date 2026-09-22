class MinStack:

    def __init__(self):
        self.stk = []
        

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append((val, val))
        else:
            curr_min = self.stk[-1][1]
            if val < curr_min:
                curr_min = val
            
            self.stk.append((val, curr_min))


    def pop(self) -> None:
        del self.stk[-1]

    def top(self) -> int:
        return self.stk[-1][0]
        
    def getMin(self) -> int:
        return self.stk[-1][1]
        
