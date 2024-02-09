class Solution(object):
    def maximumWealth(self, accounts):
        return max([sum(ind) for ind in accounts])
