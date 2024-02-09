class Solution(object):
    @staticmethod
    def countNegatives(grid):
        return sum(1 for i in grid for j in i if j < 0)
