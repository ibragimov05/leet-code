class Solution(object):
    @staticmethod
    def isThree(n):
        ls = []
        for i in range(1, n + 1):
            if n % i == 0:
                ls.append(i)
        return len(ls) == 3
