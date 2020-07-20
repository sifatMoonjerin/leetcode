class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.stack.append((x, curMin))

    def pop(self):
        self.stack.pop()
        
    def top(self):
        return self.stack[- 1][0]

    def getMin(self):
        if self.stack:
            curMin = self.stack[-1][1]
            return curMin
        return None
        