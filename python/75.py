# done
class Solution(object):
    @staticmethod
    def sortColors(nums):
        for i in range(len(nums)):
            ind = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[ind]:
                    ind = j
            nums[i], nums[ind] = nums[ind], nums[i]
        return nums
