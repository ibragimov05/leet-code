class Solution(object):
    def findTheArrayConcVal(self, nums):
        res = []
        if len(nums) % 2 != 0:
            res.append(nums[len(nums) // 2])
        for i in range(len(nums) // 2):
            res.append(int("".join(map(str, [nums[i], nums[len(nums) - 1 - i]]))))
        return sum(res)
