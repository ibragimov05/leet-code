class Solution(object):
    def singleNumber(self, nums):
        box, res = [], []
        for i in nums:
            if nums.count(i) == 3 and i not in box:
                box.append(i)
            elif nums.count(i) == 1:
                res.append(i)
                if len(res) == 2:
                    return res
