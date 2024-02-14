class Solution(object):
    def containsDuplicate(self, nums) -> bool:
        if len(set(nums)) != len(nums):
            return True
        return False
