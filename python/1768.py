class Solution(object):
    @staticmethod
    def mergeAlternately(word1, word2):
        res, ind = "", 0
        if len(word1) > len(word2):
            for i in range(len(word2)):
                res += word1[i] + word2[i]
                ind = i
            return res + word1[ind + 1:]

        for i in range(len(word1)):
            res += word1[i] + word2[i]
            ind = i
        return res + word2[ind + 1:]
