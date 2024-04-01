class Solution(object):
    def reverse(self, x):
        if x < 0:
            if self.check(int(str(abs(x))[::-1]) * -1):
                return int(str(abs(x))[::-1]) * -1
        elif x > 0 and str(x)[-1] != '0':
            if self.check(int(str(x)[::-1])):
                return int(str(x)[::-1])
        else:
            if self.check(int(str(x)[::-1])):
                return int(str(x)[::-1])
        return 0

    @staticmethod
    def check(reversed_int):
        if reversed_int < -2 ** 31 or reversed_int > 2 ** 31 - 1:
            return False
        return True
