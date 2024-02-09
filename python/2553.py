class Solution(object):
    def separateDigits(self, nums):
        ls = []
        for i in nums:
            for j in str(i):
                ls.append(int(j))
        return ls
