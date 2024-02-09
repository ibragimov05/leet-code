class Solution(object):
    def differenceOfSum(self, nums):
        return sum(nums) - sum(int(i) for i in str(''.join(map(str, nums))))