class Solution(object):
    @staticmethod
    def isAcronym(words, s):
        st = ''
        for i in range(len(words)):
            st += words[i][0]
        return st == s
