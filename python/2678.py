class Solution(object):
    def countSeniors(self, details):
        return sum(1 for each in details if int(each[11:13]) > 60)
