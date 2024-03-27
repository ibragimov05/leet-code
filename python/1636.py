class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        return sorted(nums, key=lambda x: nums.count(x))
