class Solution(object):
    @staticmethod
    def isAnagram(s, t):
        return sorted(s) == sorted(t)
