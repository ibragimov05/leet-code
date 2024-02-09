class Solution(object):
    @staticmethod
    def selfDividingNumbers(left, right):
        res = []
        for i in range(left, right + 1):
            lamp = True
            for digit in str(i):
                if not (int(digit) != 0 and i % int(digit) == 0):
                    lamp = False
                    break
            if lamp:
                res.append(i)
        return res
