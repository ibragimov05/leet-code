class Solution(object):
    def findChampion(self, grid):
        res = []
        for i in grid:
            res.append(i.count(1))
        return res.index(max(res))
