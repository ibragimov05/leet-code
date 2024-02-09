class Solution(object):
    @staticmethod
    def countConsistentStrings(allowed, words):
        cnt = 0
        for word in words:
            lamp = 1
            for each in word:
                if each not in allowed:
                    lamp = 0
            if lamp:
                cnt += 1
        return cnt
