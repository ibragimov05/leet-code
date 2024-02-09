class Solution(object):
    @staticmethod
    def smallestEvenMultiple(n):
        return n if n % 2 == 0 else n * 2
