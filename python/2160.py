class Solution(object):
    @staticmethod
    def minimumSum(num):
        num = sorted(list(str(num)))
        return int(''.join(num[0] + num[3])) + int(''.join(num[1] + num[2]))
