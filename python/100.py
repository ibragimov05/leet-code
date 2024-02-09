class Solution(object):
    def isSameTree(self, p, q):
        box1, box2 = "", ""
        for i in str(p):
            box1 += str(i)
        for i in str(q):
            box2 += str(i)
        return box1 == box2
