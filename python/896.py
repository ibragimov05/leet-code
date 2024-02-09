class Solution(object):
    def isMonotonic(self, nums):
        sor_num, rev_num = sorted(nums), sorted(nums, reverse=True)
        if rev_num == nums or sor_num == nums:
            return True
        return False
