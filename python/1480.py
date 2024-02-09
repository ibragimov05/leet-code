class Solution(object):
    @staticmethod
    def runningSum(nums):
        ls, box = [], 0
        for i in range(len(nums)):
            box += nums[i]
            ls.append(box)
        return ls
