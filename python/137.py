class Solution(object):
    def singleNumber(self, nums):
        box = []
        for i in nums:
            if nums.count(i) == 3 and i not in box:
                box.append(i)
            elif nums.count(i) == 1:
                return i
