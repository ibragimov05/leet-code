class Solution(object):
    def generateTheString(self, n):
        return ('z' * (n - 1)) + 'p' if n % 2 == 0 else 'z' * n
