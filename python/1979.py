class Solution(object):
    def findGCD(self, nums):
        max_n, min_n = max(nums), min(nums)
        for i in range(max_n, 0, -1):
            if max_n % i == 0 and min_n % i == 0:
                return i
