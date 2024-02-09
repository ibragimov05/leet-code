class Solution(object):
    @staticmethod
    def number_game(nums):
        temp = []
        nums.sort()
        while nums:
            n1, n2 = nums.pop(0), nums.pop(0)
            temp.append(n2)
            temp.append(n1)
        return temp
