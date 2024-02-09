class Solution(object):
    @staticmethod
    def missingNumber(nums):
        nums = sorted(nums).append(0)
        nums.append(0)
        for i in range(len(nums) + 1):
            if i != nums[i]:
                return i
