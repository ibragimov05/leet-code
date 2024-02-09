class Solution(object):
    @staticmethod
    def findTheDifference(s, t):
        ls1, ls2 = list(s), list(t)

        if ls1 == ls2:
            return ""
        else:
            for i in ls1:
                ls2.remove(i)
        return ls2[0]
