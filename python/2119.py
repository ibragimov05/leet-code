class Solution(object):
    @staticmethod
    def isSameAfterReversals(num):
        if '0' == str(num)[-1] and str(num) != "0":
            return False
        else:
            return True
