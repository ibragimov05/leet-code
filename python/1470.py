class Solution(object):
    def shuffle(self, nums, n):
        box = []
        for i in range(n):
            box.append(nums[i])
            box.append(nums[n])
            n += 1
        return box
