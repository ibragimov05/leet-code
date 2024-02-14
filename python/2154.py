class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        while True:
            if original not in nums:
                return original
            if original in nums:
                original *= 2
