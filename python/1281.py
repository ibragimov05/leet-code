class Solution(object):
    @staticmethod
    def subtractProductAndSum(n):
        plus, multiply = 0, 1
        for i in str(n):
            plus += int(i)
            multiply *= int(i)
        return multiply - plus
