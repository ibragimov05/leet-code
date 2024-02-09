class Solution(object):
    def prefixCount(self, words, pref):
        cnt = 0
        for i in words:
            if i.startswith(pref):
                cnt += 1
        return cnt
