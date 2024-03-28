class Solution(object):
    def firstMissingPositive(self, nums) -> int:
        num_set = set(nums)
        smallest_positive = 1

        while smallest_positive in num_set:
            smallest_positive += 1

        return smallest_positive
