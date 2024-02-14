class Solution(object):
    def numOfStrings(self, patterns, word):
        return sum(1 for i in patterns if i in word)
