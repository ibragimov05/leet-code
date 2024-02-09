class MinStack(object):

    def __init__(self):
        self.ls = []

    def push(self, val):
        return self.ls.append(val)

    def pop(self):
        return self.ls.pop()

    def top(self):
        return self.ls[-1]

    def getMin(self):
        return min(self.ls)
