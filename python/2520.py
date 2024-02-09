class Solution(object):
    def countDigits(self, num):
        return sum(1 for i in str(num) if num % int(i) == 0)
