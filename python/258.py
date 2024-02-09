class Solution(object):
    def addDigits(self, num):
        while num > 9:
            list_of_digits = [int(i) for i in str(num)]
            num = sum(list_of_digits)
        return num
