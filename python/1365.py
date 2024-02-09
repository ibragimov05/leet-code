class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        box = []
        for i in nums:
            cnt = 0
            for j in nums:
                if i > j:
                    cnt += 1
            box.append(cnt)
        return box
