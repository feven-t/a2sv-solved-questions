class MinStack:

    def __init__(self):
        self.s =[]
        self.m =[]
        

    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.m )== 0 or val<=self.m[-1]:
            self.m.append(val)
        

    def pop(self) -> None:
        val = self.s.pop()
        if self.m[-1] == val:
            self.m.pop()
        return val

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.m[-1]
