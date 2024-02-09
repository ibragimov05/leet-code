class MyQueue(object):

    def __init__(self):
        self.ls = []

    def push(self, x):
        return self.ls.append(x)

    def pop(self):
        return self.ls.pop(0)

    def peek(self):
        return self.ls[0]

    def empty(self):
        return len(self.ls) == 0
