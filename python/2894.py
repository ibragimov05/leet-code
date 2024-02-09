class Solution(object):
    @staticmethod
    def differenceOfSums(n, m):
        divisible, non_divisible = 0, 0
        for i in range(1, n + 1):
            if i % m == 0:
                divisible += i
            else:
                non_divisible += i
        return non_divisible - divisible
