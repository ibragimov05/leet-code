class Solution(object):
    def countOperations(self, num1, num2):
        if num1 == num2 and num1 != 0:
            return 1
        elif num1 == 0 or num2 == 0:
            return 0
        res = 0
        while num1 != 0 or num2 != 0:
            if num1 < num2:
                num2 = num2 - num1
                res += 1
            elif num1 > num2:
                num1 = num1 - num2
                res += 1
            else:
                res += 1
                return res
