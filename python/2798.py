class Solution(object):
    @staticmethod
    def numberOfEmployeesWhoMetTarget(hours, target):
        return sum(1 for i in hours if i >= target)
